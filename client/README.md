# Running the client

Note: Docker is must needed for this setup to run

Currently since I created the crawler service in docker and running this shell script the way described below will run client python script and also download the file from minio S3 storage.

The shell script takes two arguments as described below url and output

This is to make sure all python version dependencies are met.

Note: The output is piped to stdout only after command completion. For better and continuous output please run the python script directly


### Client run
```bash
client git:(main) ✗ ./run-crawler.sh --url "https://www.mockaroo.com/" --output "sitemap.json"
[+] Building 8.7s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 37B                                                                                                                          0.0s
 => [internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.11-bookworm                                                                                      0.8s
 => [internal] load build context                                                                                                                            0.0s
 => => transferring context: 34.28kB                                                                                                                         0.0s
 => [1/4] FROM docker.io/library/python:3.11-bookworm@sha256:62a79bedce9ebc0a6034e6f0819ec19dfa0ecaea187ad45712828aa8749c4f4e                                0.0s
 => CACHED [2/4] WORKDIR /usr/src/app                                                                                                                        0.0s
 => [3/4] COPY . .                                                                                                                                           0.0s
 => [4/4] RUN pip install --no-cache-dir requests                                                                                                            7.5s
 => exporting to image                                                                                                                                       0.2s
 => => exporting layers                                                                                                                                      0.2s
 => => writing image sha256:15523bc918b2dc45b8ec9a76cc4a400b5e88517c848bf4018787cc2aaa6c7403                                                                 0.0s
 => => naming to docker.io/library/crawler-client                                                                                                            0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
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
Task status: PENDING. Checking again in 5 seconds...
Downloading url: http://minio:9000/sitemaps/6161fwww.mockaroo.com.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MINIO_ACCESS_KEY%2F20240801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240801T121140Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=39add51db645f65a597274b69cb95ce58c09c3032f892a01bd65ef7e87c76e72
<Response [200]>
Sitemap downloaded to sitemap.json
Storing the sitemap in the current folder
crawler-client
crawler-client
```

### Second time run (Data coming from cache)
```bash
  client git:(main) ✗ ./run-crawler.sh --url "https://www.mockaroo.com/" --output "sitemap.json"
Image found. Skipping build...
Submitting crawl task for URL: https://www.mockaroo.com/
Got response: {'task_id': '', 'sitemap_url': 'http://minio:9000/sitemaps/6161fwww.mockaroo.com.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MINIO_ACCESS_KEY%2F20240801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240801T121140Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=39add51db645f65a597274b69cb95ce58c09c3032f892a01bd65ef7e87c76e72'}
Downloading url: http://minio:9000/sitemaps/6161fwww.mockaroo.com.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MINIO_ACCESS_KEY%2F20240801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240801T121140Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=39add51db645f65a597274b69cb95ce58c09c3032f892a01bd65ef7e87c76e72
<Response [200]>
Sitemap downloaded to sitemap.json
Storing the sitemap in the current folder
crawler-client
crawler-client
```

### Local run without shell script
Note: Only the download of sitemap fails as it is not directly exposed from minio s3 bucket

```bash
client git:(main) ✗ python local_client.py --url "https://www.mockaroo.com/" --output "sitemap.json"
Submitting crawl task for URL: https://www.mockaroo.com/
Got response: {'task_id': '', 'sitemap_url': 'http://minio:9000/sitemaps/6161fwww.mockaroo.com.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MINIO_ACCESS_KEY%2F20240801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240801T121140Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=39add51db645f65a597274b69cb95ce58c09c3032f892a01bd65ef7e87c76e72'}
Downloading url: http://minio:9000/sitemaps/6161fwww.mockaroo.com.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=MINIO_ACCESS_KEY%2F20240801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240801T121140Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=39add51db645f65a597274b69cb95ce58c09c3032f892a01bd65ef7e87c76e72
```
