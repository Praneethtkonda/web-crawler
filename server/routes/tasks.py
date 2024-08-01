from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from worker import crawler_task
from schemas.tasks import SubmitCrawlingTask, CrawlResponse, TaskInfo, TaskStatus
import redis
import os

# Environment variables
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")

# Redis client
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

router = APIRouter()

@router.get("/health")
def health_check():
    result = {"Response": "Up and running"}
    return JSONResponse(result)

@router.post(
    path="/crawl",
    status_code=200,
    response_model=CrawlResponse
)
def submit_crawling_task(
    payload: SubmitCrawlingTask
):
    """
    Submit a message or previously-uploaded file to be signed asynchronously.
    The returned task ID can be used to query the status of the task.
    """

    cached_url = redis_client.get(payload.url)
    if cached_url:
        print("Found url in cache")
        return CrawlResponse(task_id="", sitemap_url=cached_url)
    
    task = crawler_task.delay(payload_dict=payload.dict())
    print(task.state)
    return CrawlResponse(task_id=task.id, sitemap_url="")

@router.get(
        path="/tasks/{task_id}",
        response_model=TaskInfo,
        operation_id="getTaskStatus",
        summary="Get status of a task",
    )
def get_status(task_id: str):
    task = crawler_task.AsyncResult(task_id)

    state = task.state
    error_message = None
    download_url = ""
    input_url = ""

    if state == TaskStatus.PENDING:
        return TaskInfo(task_id=task_id, status=state)
    elif state == TaskStatus.FAILURE:
        input_url = task.input_url
        error_message = str(task.error_message)
    elif state == TaskStatus.SUCCESS:
        download_url = task.result["sitemap_url"]
        input_url = task.result["input_url"]
    else:
        error_message = f"Task state: {state}"

    return TaskInfo(
        task_id=task_id,
        status=state,
        timestamp="",  # Add a timestamp if you have one
        input_url=input_url,
        sitemap_url=download_url,
        error_message=error_message,
    )