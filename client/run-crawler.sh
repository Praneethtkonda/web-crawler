#!/bin/bash

# Variables
NETWORK_NAME=web-crawler_default
IMAGE_NAME=crawler-client
CONTAINER_NAME=crawler-client

# Get URL from command line argument
URL=$2
OUTPUT=$4

# Check if URL is provided
if [ -z "$URL" ]; then
  echo "Usage: $0 --url <url_to_be_crawled> --output <output_file_name>"
  exit 1
fi

if [ -z "$OUTPUT" ]; then
  echo "Usage: $0 --url <url_to_be_crawled> --output <output_file_name>"
  exit 1
fi

# echo $URL
# echo $OUTPUT

COMMAND="python client.py $@" 

# Build the Docker image
# Check if the image already exists
if ! docker images | grep -q "$IMAGE_NAME"; then
  echo "Image not found. Building the Docker image..."
  docker build -t $IMAGE_NAME .
else
  echo "Image found. Skipping build..."
fi

# Run the Docker container with the provided URL
docker run --network $NETWORK_NAME --name $CONTAINER_NAME $IMAGE_NAME bash -c "$COMMAND"
echo "Storing the sitemap in the current folder"
docker cp $CONTAINER_NAME:/usr/src/app/$OUTPUT ./$OUTPUT
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
