# Running the server

Note: Docker is must needed for this setup to work and run

Navigate to the server folder and run docker compose up to bring
up the containers.

The server is a container setup consisting of the following containers
1. redis => For message queue and caching information.
2. minio => For storing sitemaps and exporting them to client via pre signed URLs.
3. api => The API server which listens to incoming requests and enqueues any crawling task.
          It also exposes the tasks route for querying the status of the request.
4. worker => Worker stateless containers which does the heavy lifting of crawling the URLs
            and storing the results in redis and minio object store.
5. dashboard => Flower monitoring dashboard for monitoring celery tasks.

```bash
web-crawler/server % docker compose up
[+] Running 18/18
 ✔ minio Pulled                                                                                                                                                                                       65.8s 
   ✔ 5f328c14e09d Pull complete                                                                                                                                                                        9.7s 
   ✔ ce5a3cfe4817 Pull complete                                                                                                                                                                        9.7s 
   ✔ d6417525014d Pull complete                                                                                                                                                                       59.3s 
   ✔ dab361c1704a Pull complete                                                                                                                                                                       60.1s 
   ✔ d5b34025ed42 Pull complete                                                                                                                                                                       60.3s 
   ✔ 246567e678bf Pull complete                                                                                                                                                                       60.4s 
   ✔ 9e79d854f95f Pull complete                                                                                                                                                                       60.4s 
   ✔ 782190a7e622 Pull complete                                                                                                                                                                       60.4s 
 ✔ redis Pulled                                                                                                                                                                                       68.5s 
   ✔ efc2b5ad9eec Pull complete                                                                                                                                                                       61.1s 
   ✔ 82797145fff6 Pull complete                                                                                                                                                                       61.1s 
   ✔ 405e1ffae71e Pull complete                                                                                                                                                                       61.2s 
   ✔ 0beb16fe974a Pull complete                                                                                                                                                                       61.7s 
   ✔ 73eb92ddeed3 Pull complete                                                                                                                                                                       63.0s 
   ✔ 87e613039f4a Pull complete                                                                                                                                                                       63.0s 
   ✔ 4f4fb700ef54 Pull complete                                                                                                                                                                       63.0s 
   ✔ 9579b898bbe4 Pull complete                                                                                                                                                                       63.1s 
[+] Building 162.2s (7/15)                                                                                                                                                             docker:desktop-linux
[+] Building 164.2s (7/15)                                                                                                                                                             docker:desktop-linux
[+] Building 165.1s (7/15)                                                                                                                                                             docker:desktop-linux
[+] Building 175.7s (7/15)                                                                                                                                                             docker:desktop-linux
[+] Building 176.6s (7/15)                                                                                                                                                             docker:desktop-linux
[+] Building 307.2s (21/24)                                                                                                                                                            docker:desktop-linux
 => [worker internal] load build definition from Dockerfile.celery_worker                                                                                                                              0.1s
 => => transferring dockerfile: 236B                                                                                                                                                                   0.0s
 => [api internal] load build definition from Dockerfile.api_server                                                                                                                                    0.1s
 => => transferring dockerfile: 243B                                                                                                                                                                   0.0s
 => [dashboard internal] load metadata for docker.io/library/python:3.11-bookworm                                                                                                                      6.7s
 => [worker internal] load .dockerignore                                                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                                                        0.0s
 => [api internal] load .dockerignore                                                                                                                                                                  0.1s
 => => transferring context: 2B                                                                                                                                                                        0.0s
 => [dashboard 1/5] FROM docker.io/library/python:3.11-bookworm@sha256:62a79bedce9ebc0a6034e6f0819ec19dfa0ecaea187ad45712828aa8749c4f4e                                                              188.0s
 => => resolve docker.io/library/python:3.11-bookworm@sha256:62a79bedce9ebc0a6034e6f0819ec19dfa0ecaea187ad45712828aa8749c4f4e                                                                          0.1s
 => => sha256:ca4e5d6727252f0dbc207fbf283cb95e278bf562bda42d35ce6c919583a110a0 49.55MB / 49.55MB                                                                                                      70.7s
 => => sha256:10d643a5fa823cd013a108b2076f4d2edf1b2a921f863b533e83ea5ed8d09bd4 64.14MB / 64.14MB                                                                                                      75.8s
 => => sha256:62a79bedce9ebc0a6034e6f0819ec19dfa0ecaea187ad45712828aa8749c4f4e 9.07kB / 9.07kB                                                                                                         0.0s
 => => sha256:5393dd665963a555911529f7a84a9358f01f8277b622ff1b7ce02c5ad5856f57 7.27kB / 7.27kB                                                                                                         0.0s
 => => sha256:ae53e69f6d40dddd0ff46d3d0ee69e7d4d70cc6955bbe9ef4d90fbda74e6444c 2.52kB / 2.52kB                                                                                                         0.0s
 => => sha256:30b93c12a9c9326732b35d9e3ebe57148abe33f8fa6e25ab76867410b0ccf876 24.05MB / 24.05MB                                                                                                      24.6s
 => => sha256:d6dc1019d7935fe82827434da11bf96cf14e24979f8155e73b794286f10b7f05 211.24MB / 211.24MB                                                                                                   161.8s
 => => sha256:3f97c2dcac68ff3d5491ff1aad4ab18fee8d8dc2363c4c0d968517b53315c9b6 6.16MB / 6.16MB                                                                                                        77.6s
 => => extracting sha256:ca4e5d6727252f0dbc207fbf283cb95e278bf562bda42d35ce6c919583a110a0                                                                                                              8.5s
 => => sha256:10b660d66aedc5cdf320443baa5fcbf67df2800e164d1b30ec5f6ff63e285539 19.84MB / 19.84MB                                                                                                     106.8s
 => => sha256:3c06c666a70df3fd16fa0005fda89ea04d109b57bb02620f3d8f9d6c9130b684 230B / 230B                                                                                                            78.7s
 => => sha256:28fd036baf971132325c21f5eb777faf21dc1d1ce4961fb96233f9eaa1267ebe 3.13MB / 3.13MB                                                                                                        85.6s
 => => extracting sha256:30b93c12a9c9326732b35d9e3ebe57148abe33f8fa6e25ab76867410b0ccf876                                                                                                              1.9s
 => => extracting sha256:10d643a5fa823cd013a108b2076f4d2edf1b2a921f863b533e83ea5ed8d09bd4                                                                                                             12.1s
 => => extracting sha256:d6dc1019d7935fe82827434da11bf96cf14e24979f8155e73b794286f10b7f05                                                                                                             21.6s
 => => extracting sha256:3f97c2dcac68ff3d5491ff1aad4ab18fee8d8dc2363c4c0d968517b53315c9b6                                                                                                              0.8s
 => => extracting sha256:10b660d66aedc5cdf320443baa5fcbf67df2800e164d1b30ec5f6ff63e285539                                                                                                              2.0s
 => => extracting sha256:3c06c666a70df3fd16fa0005fda89ea04d109b57bb02620f3d8f9d6c9130b684                                                                                                              0.0s
 => => extracting sha256:28fd036baf971132325c21f5eb777faf21dc1d1ce4961fb96233f9eaa1267ebe                                                                                                              0.8s
 => [worker internal] load build context                                                                                                                                                               0.1s
 => => transferring context: 16.98kB                                                                                                                                                                   0.0s
 => [api internal] load build context                                                                                                                                                                  0.1s
 => => transferring context: 16.98kB                                                                                                                                                                   0.0s
 => CACHED [dashboard 2/5] WORKDIR /app                                                                                                                                                                1.8s
 => [api 3/5] COPY ./requirements.txt .                                                                                                                                                                0.0s
 => [worker 4/5] RUN pip install -r requirements.txt                                                                                                                                                 107.9s
 => [api 5/5] COPY . .                                                                                                                                                                                 0.1s
 => [worker] exporting to image                                                                                                                                                                        1.7s 
 => => exporting layers                                                                                                                                                                                1.7s 
 => => writing image sha256:b3c2dc5cf5ce16b216fb5f0b471f465c53b46c86895b41cb22d27998f0a6a505                                                                                                           0.0s 
 => => naming to docker.io/library/web-crawler-worker                                                                                                                                                  0.0s 
 => [api] exporting to image                                                                                                                                                                           1.7s 
 => => exporting layers                                                                                                                                                                                1.7s
 => => writing image sha256:4e3cbdd14dda5f4e4668a6e557a4e6a5f9a6d81019be0cb172b16d83fbf77ce7                                                                                                           0.0s
 => => naming to docker.io/library/web-crawler-api                                                                                                                                                     0.0s
 => [dashboard internal] load build definition from Dockerfile.celery_worker                                                                                                                           0.0s
 => => transferring dockerfile: 236B                                                                                                                                                                   0.0s
 => [dashboard internal] load .dockerignore                                                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                                                        0.0s
 => [dashboard internal] load build context                                                                                                                                                            0.0s
 => => transferring context: 692B                                                                                                                                                                      0.0s
 => CACHED [dashboard 3/5] COPY ./requirements.txt .                                                                                                                                                   0.0s
 => CACHED [dashboard 4/5] RUN pip install -r requirements.txt                                                                                                                                         0.0s
 => CACHED [dashboard 5/5] COPY . .                                                                                                                                                                    0.0s
 => [dashboard] exporting to image                                                                                                                                                                     0.0s
 => => exporting layers                                                                                                                                                                                0.0s
 => => writing image sha256:63e6cf0478c881b5c7c604550705cceabb0f65bd98e281c7559d178806980f49                                                                                                           0.0s
 => => naming to docker.io/library/web-crawler-dashboard                                                                                                                                               0.0s
[+] Running 6/6
 ✔ Network web-crawler_default        Created                                                                                                                                                          0.1s 
 ✔ Container web-crawler-minio-1      Created                                                                                                                                                          0.2s 
 ✔ Container web-crawler-redis-1      Created                                                                                                                                                          0.2s 
 ✔ Container web-crawler-worker-1     Created                                                                                                                                                          0.2s 
 ✔ Container web-crawler-api-1        Created                                                                                                                                                          0.2s 
 ✔ Container web-crawler-dashboard-1  Created                                                                                                                                                          0.1s 
Attaching to api-1, dashboard-1, minio-1, redis-1, worker-1
redis-1      | 1:C 01 Aug 2024 15:08:57.470 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis-1      | 1:C 01 Aug 2024 15:08:57.471 * Redis version=7.4.0, bits=64, commit=00000000, modified=0, pid=1, just started
redis-1      | 1:C 01 Aug 2024 15:08:57.471 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis-1      | 1:M 01 Aug 2024 15:08:57.472 * monotonic clock: POSIX clock_gettime
redis-1      | 1:M 01 Aug 2024 15:08:57.474 * Running mode=standalone, port=6379.
redis-1      | 1:M 01 Aug 2024 15:08:57.475 * Server initialized
redis-1      | 1:M 01 Aug 2024 15:08:57.475 * Ready to accept connections tcp
minio-1      | INFO: WARNING: MINIO_ACCESS_KEY and MINIO_SECRET_KEY are deprecated.
minio-1      |          Please use MINIO_ROOT_USER and MINIO_ROOT_PASSWORD
minio-1      | INFO: Formatting 1st pool, 1 set(s), 1 drives per set.
minio-1      | INFO: WARNING: Host local has more than 0 drives of set. A host failure will result in data becoming unavailable.
minio-1      | MinIO Object Storage Server
minio-1      | Copyright: 2015-2024 MinIO, Inc.
minio-1      | License: GNU AGPLv3 - https://www.gnu.org/licenses/agpl-3.0.html
minio-1      | Version: RELEASE.2024-07-31T05-46-26Z (go1.22.5 linux/amd64)
minio-1      | 
minio-1      | API: http://172.18.0.3:9000  http://127.0.0.1:9000 
minio-1      | WebUI: http://172.18.0.3:9001 http://127.0.0.1:9001  
minio-1      | 
minio-1      | Docs: https://min.io/docs/minio/linux/index.html
api-1        | INFO:     Started server process [1]
api-1        | INFO:     Waiting for application startup.
api-1        | INFO:     Application startup complete.
api-1        | INFO:     Uvicorn running on http://0.0.0.0:3005 (Press CTRL+C to quit)
worker-1     | /usr/local/lib/python3.11/site-packages/celery/platforms.py:829: SecurityWarning: You're running the worker with superuser privileges: this is
worker-1     | absolutely not recommended!
worker-1     | 
worker-1     | Please specify a different user using the --uid option.
worker-1     | 
worker-1     | User information: uid=0 euid=0 gid=0 egid=0
worker-1     | 
worker-1     |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
worker-1     |  
worker-1     |  -------------- celery@eb02fc71b595 v5.4.0 (opalescent)
worker-1     | --- ***** ----- 
worker-1     | -- ******* ---- Linux-6.6.32-linuxkit-x86_64-with-glibc2.36 2024-08-01 15:09:01
worker-1     | - *** --- * --- 
worker-1     | - ** ---------- [config]
worker-1     | - ** ---------- .> app:         worker:0x7f9140aff0d0
worker-1     | - ** ---------- .> transport:   redis://redis:6379/0
worker-1     | - ** ---------- .> results:     redis://redis:6379/0
worker-1     | - *** --- * --- .> concurrency: 4 (prefork)
worker-1     | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
worker-1     | --- ***** ----- 
worker-1     |  -------------- [queues]
worker-1     |                 .> celery           exchange=celery(direct) key=celery
worker-1     |                 
worker-1     | 
worker-1     | [tasks]
worker-1     |   . clean_tmp_file
worker-1     |   . crawler_task
worker-1     |   . health_celery_task
worker-1     | 
dashboard-1  | [I 240801 15:09:01 command:152] Visit me at http://localhost:5555
dashboard-1  | [I 240801 15:09:01 command:159] Broker: redis://redis:6379/0
dashboard-1  | [I 240801 15:09:01 command:160] Registered tasks: 
dashboard-1  |     ['celery.accumulate',
dashboard-1  |      'celery.backend_cleanup',
dashboard-1  |      'celery.chain',
dashboard-1  |      'celery.chord',
dashboard-1  |      'celery.chord_unlock',
dashboard-1  |      'celery.chunks',
dashboard-1  |      'celery.group',
dashboard-1  |      'celery.map',
dashboard-1  |      'celery.starmap',
dashboard-1  |      'clean_tmp_file',
dashboard-1  |      'crawler_task',
dashboard-1  |      'health_celery_task']
dashboard-1  | [I 240801 15:09:01 mixins:228] Connected to redis://redis:6379/0
worker-1     | [2024-08-01 15:09:02,350: WARNING/MainProcess] /usr/local/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:508: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
worker-1     | whether broker connection retries are made during startup in Celery 6.0 and above.
worker-1     | If you wish to retain the existing behavior for retrying connections on startup,
worker-1     | you should set broker_connection_retry_on_startup to True.
worker-1     |   warnings.warn(
worker-1     | 
worker-1     | [2024-08-01 15:09:02,376: INFO/MainProcess] Connected to redis://redis:6379/0
worker-1     | [2024-08-01 15:09:02,379: WARNING/MainProcess] /usr/local/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:508: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
worker-1     | whether broker connection retries are made during startup in Celery 6.0 and above.
worker-1     | If you wish to retain the existing behavior for retrying connections on startup,
worker-1     | you should set broker_connection_retry_on_startup to True.
worker-1     |   warnings.warn(
worker-1     | 
worker-1     | [2024-08-01 15:09:02,394: INFO/MainProcess] mingle: searching for neighbors
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method stats failed
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method scheduled failed
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method revoked failed
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method active_queues failed
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method reserved failed
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method active failed
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method conf failed
dashboard-1  | [W 240801 15:09:03 inspector:42] Inspect method registered failed
worker-1     | [2024-08-01 15:09:03,420: INFO/MainProcess] mingle: all alone
worker-1     | [2024-08-01 15:09:03,446: INFO/MainProcess] celery@eb02fc71b595 ready.
worker-1     | [2024-08-01 15:09:06,890: INFO/MainProcess] Events of group {task} enabled by remote.
api-1        | INFO:     192.168.65.1:25100 - "GET /api/v1/docs HTTP/1.1" 200 OK
api-1        | INFO:     192.168.65.1:25100 - "GET /api/v1/docs/openapi.json HTTP/1.1" 200 OK
api-1        | INFO:     192.168.65.1:22255 - "GET /api/v1/health HTTP/1.1" 200 OK
worker-1     | [2024-08-01 15:11:26,462: INFO/MainProcess] Task crawler_task[6c39f464-c6ea-4cd1-9889-8c9243ccb1a7] received
api-1        | PENDING

```

