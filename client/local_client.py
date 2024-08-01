import requests
import argparse
import time
import os

from datetime import datetime

API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:3005/api/v1")
TIMEOUT = 60 * 10 # 10 minutes

def parse_arguments():
    parser = argparse.ArgumentParser(description="Crawl the whole website based on input_url")
    parser.add_argument('--url', help='URL to be crawled')
    parser.add_argument('--output', help='Output filename for the sitemap to be stored')
    return parser.parse_args()

def submit_crawl_task(url):
    response = requests.post(f"{API_BASE_URL}/crawl", json={"url": url, "max_ttr": 30})
    response.raise_for_status()
    return response.json()

def check_task_status(task_id):
    response = requests.get(f"{API_BASE_URL}/tasks/{task_id}")
    response.raise_for_status()
    return response.json()

def download_sitemap(download_url, filename):
    print(f"Downloading url: {download_url}")
    response = requests.get(download_url)
    print(response)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Sitemap downloaded to {filename}")

def main():
    args = parse_arguments()
    url = args.url
    output_location = args.output

    if not url or not output_location:
        print("Error missing arugments. Please recheck")
        return 1

    print(f"Submitting crawl task for URL: {url}")
    crawl_response = submit_crawl_task(url)
    print(f"Got response: {crawl_response}")

    if "sitemap_url" in crawl_response and crawl_response["sitemap_url"] != "":
        # URL found in cache, download directly
        download_url = crawl_response["sitemap_url"]
        download_sitemap(download_url, output_location)
    else:
        # Get task ID and poll for status
        task_id = crawl_response["task_id"]
        print(f"Task ID: {task_id}")
        print("Waiting for task to complete...")

        start_time = datetime.now()
        while True:
            time_delta = datetime.now() - start_time

            if time_delta.total_seconds() >= TIMEOUT:
                print("Timeout calling API. So, stopping the retries")
                break

            task_status = check_task_status(task_id)
            if task_status["status"] == "SUCCESS":
                download_url = task_status["sitemap_url"]
                download_sitemap(download_url, output_location)
                break
            elif task_status["status"] == "FAILURE":
                print("Task failed.")
                break
            else:
                print(f"Task status: {task_status['status']}. Checking again in 5 seconds...")
                time.sleep(3)

if __name__ == "__main__":
    main()
