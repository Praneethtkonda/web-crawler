FROM python:3.11-bookworm

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir requests

# Run an infinite loop to keep the container running
CMD ["tail", "-f", "/dev/null"]