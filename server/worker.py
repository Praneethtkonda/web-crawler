import os
import redis
import minio

from celery import Celery
from util.crawler import WebCrawler
from util.helper import create_unique_file_name, get_netloc
from schemas.tasks import SubmitCrawlingTask, TaskResult

# TODO: Manage this properly
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
MINIO_HOST = os.environ.get("MINIO_HOST", "minio")
MINIO_PORT = os.environ.get("MINIO_PORT", "9000")
MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY", "MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY", "MINIO_SECRET_KEY")


celery = Celery(__name__)
celery_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
celery.conf.broker_url = celery_url
celery.conf.result_backend = celery_url
celery.conf.result_extended = True

# Redis client
CACHE_EXPIRATION = 3600  # Cache expiration time in seconds (1 hour)
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

# MinIO client
minio_client = minio.Minio(
    f"{MINIO_HOST}:{MINIO_PORT}",
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

BUCKET_NAME = "sitemaps"
if not minio_client.bucket_exists(BUCKET_NAME):
    minio_client.make_bucket(BUCKET_NAME)


@celery.task(name="health_celery_task")
def health_celery_task():
    return {"Status": "Working"}

@celery.task(name="clean_tmp_file")
def clean_tmp_file(file_location):
    if os.path.exists(file_location):
        os.remove(file_location)

@celery.task(name="crawler_task")
def crawler_task(payload_dict):
    try:
        payload = SubmitCrawlingTask(**payload_dict)

        web_crawler = WebCrawler(payload.url, max_threads=10)
        web_crawler.crawl()
        web_crawler.print_urls()

        url_base_domain = get_netloc(payload.url).strip("/")
        file_name = create_unique_file_name(url_base_domain, extension=".json")
        file_path = os.path.join("/tmp", file_name)
        
        web_crawler.export_site_map_json(file_path)

        minio_client.fput_object(
            BUCKET_NAME,
            file_name,
            file_path
        )

        url = minio_client.presigned_get_object(BUCKET_NAME, file_name)
        print("Storing the result in cache")
        redis_client.setex(payload.url, CACHE_EXPIRATION, url)  # Cache result for 1 hour

        result = {"state": "SUCCESS", "input_url": payload.url, "sitemap_url": url, "error_message": ""}
        clean_tmp_file.delay(file_path)
    except Exception as e:
        result = {"state": "FAILED", "input_url": payload.url, "sitemap_url": "", "error_message": str(e)}
    finally:
        return result
