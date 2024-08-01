# web-crawler
A simple web crawler service including both server and client

# Running client and server
Instructions for client:
1. Navigate to the client folder.
2. Run the run-crawler.sh shell script with url and output arguments to get the 
   sitemap in the same folder with the name provided by you.

Instructions for server:
1. Run the docker compose up command on the root folder to bring up all the dependent containers.
2. Once the containers are up and running, you can check for swagger documentation of API.
3. Visit localhost:3005/api/v1/docs for server documentation and interaction.
4. Visit localhost:9001 for minio.
5. Visit localhost:5556 for flower monitoring dashboard to monitor crawling tasks that are queued.


For more information and detailed runs refer to these links:-

For client documentation refer [here](./client/README.md)

For server documentation refer [here](./server/README.md)

# Current flow

The flow goes like this

1. If the request is not in cache the request will be sent to the server worker crawler to crawl and the client gets an task_id for tracking.
2. Once the crawler's job is done the task status gets updated and the client will track the status of the job and once completed it will download the sitemap.
3. If present in the cache the client gets the pre_signed url from S3 bucket to download the site map and client can download the sitemap.

# Architecture
![Alt text](./Archi.png "Archite")

# Running tests
```bash
docker compose exec -ti worker bash -c "python -m unittest discover -s tests"
```

# Advantages of this approach
1. The approach is a hybrid of both sync and async approach. Synchronous when the cache is populated with sitemap for a given url. Async task based approach when the crawling request is for the first time.
2. The server is capable running multiple web crawling tasks.
3. Also since the workers are stateless horizontal scaling is also possible.
4. Storage of sitemap is done on an object storage and the client later is presented with presigned url of the file.

# Limitations of this approach

1. As of now the we are using minio for s3 subsitution
2. The crawler is written in python where I leveraged threadpool but the performance can be improved.
