# Running the client

Note: Docker is must needed for this setup to run

For the client to work, make sure the server containers are up and running. 
If not please refer to [here](../server/README.md)

### Running the python script directly

Note: Python3 is necessary to run this script directly
```bash
client git:(main) ✗ pip install requests # This step is necessary
client git:(main) ✗ python client.py --url "https://www.mockaroo.com/" --output "sitemap.json"
Submitting crawl task for URL: https://www.mockaroo.com/
Got response: {'task_id': '5262585e-a99e-46b4-a3ff-ee051f12443d', 'sitemap_url': ''}
Task ID: 5262585e-a99e-46b4-a3ff-ee051f12443d
Waiting for task to complete...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...
Task status: PENDING. Checking again in 5 seconds...X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MINIO_ACCESS_KEY%2F20240802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240802T094411Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a7916602741efb8418c972308fe24683140cc42f3f4d0f2bf14a7761ffe60d71'}
Downloading url: http://localhost:8080/sitemaps/e872fwww.mockaroo.com.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MINIO_ACCESS_KEY%2F20240802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240802T094411Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a7916602741efb8418c972308fe24683140cc42f3f4d0f2bf14a7761ffe60d71
<Response [200]>
Sitemap downloaded to sitemap.json
```


### Running the client executable

Note: The executable is generated via pyinstaller. 
Pls run the ./bin/crawl_client_linux if you are on a linux machine
Pls run the ./bin/crawl_client_mac if you are on a mac machine

Run for linux machine
```bash
root@43f7b2ff6305:/web-crawler/client$ ./bin/crawl_client_linux --help
usage: crawl_client_linux [-h] [--url URL] [--output OUTPUT]

Crawl the whole website based on input_url

options:
  -h, --help       show this help message and exit
  --url URL        URL to be crawled
  --output OUTPUT  Output filename for the sitemap to be stored
```

Run for mac machine
```bash
➜  client git:(main) ✗ ./bin/crawl_client_mac --help
usage: crawl_client_mac [-h] [--url URL] [--output OUTPUT]

Crawl the whole website based on input_url

optional arguments:
  -h, --help       show this help message and exit
  --url URL        URL to be crawled
  --output OUTPUT  Output filename for the sitemap to be stored
```