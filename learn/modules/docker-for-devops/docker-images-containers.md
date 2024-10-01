---
title: "Docker Images and Containers"
---
**Docker Image**

A Docker image is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, runtime, libraries, dependencies, and system tools. Docker images are built from a set of instructions called a Dockerfile, which specifies the steps needed to create the image.

Here are some key concepts related to Docker images:

1.  **Containerization:** Docker uses containerization technology to package applications and their dependencies into a container. A container is a runnable instance of a Docker image.
    

2.  **Dockerfile:** A Dockerfile is a text document that contains instructions for building a Docker image. It specifies the base image, sets up the environment, installs dependencies, and defines how the application should run.
    

3.  **Layers:** Docker images are built in layers, and each instruction in the Dockerfile adds a new layer to the image. Layers are cached, and if a Dockerfile hasn't changed, Docker can reuse existing layers, making the build process more efficient.
    

4.  **Registry:** Docker images can be stored and shared through a registry. Docker Hub is a popular public registry, but you can also set up private registries for more control over image distribution.
    

5.  **Base Image:** The starting point for a Docker image is often a base image that provides a minimal operating system environment. Common base images include Alpine Linux, Ubuntu, and others.
    

6.  **Tag:** Docker images can have tags to differentiate between different versions or configurations of the same application. For example, an image might have tags like "latest," "v1.0," or "development."
    

1.  **Pulling Docker Images:**
    
Pulling an Image from Docker Hub:
docker pull imageName:tag
Example: docker pull ubuntu:latest

2. **Listing Docker Images:**

Listing Downloaded Images:_
docker images

3. **Removing Docker Images:**

Removing an Image:_
docker rmi imageName:tag
Example: docker rmi ubuntu:latest

Removing All Unused Images:_
docker image prune

4. **Tagging Docker Images:**

Tagging an Image:_
docker tag sourceImage:tag targetImage:tag
Example: docker tag ubuntu:latest my-ubuntu:latest

5. **Building Docker Images:**

Building an Image from a Dockerfile:_
docker build -t imageName:tag path/to/Dockerfile Example: docker build -t my-node-app:latest .

6. **Inspecting Docker Images:**

Inspecting Image Metadata:_
docker image inspect imageName:tag
Example: docker image inspect ubuntu:latest

Displaying Image Layers:_
docker image history imageName:tag
Example: docker image history ubuntu:latest

7. **Saving and Loading Docker Images:**

Saving an Image to a TAR file:_
docker save -o output.tar imageName:tag
Example: docker save -o ubuntu latest.tar ubuntu:latest

Loading an Image from a TAR file:_
docker load -i input.tar
Example: docker load -i ubuntu\_latest.tar

8. **Exporting and Importing Docker Images:**

Exporting an Image to a TAR file:_
docker export -o output.tar containerName
Example: docker export -o ubuntu container.tar ubuntu container

Importing an Image from a TAR file:_

docker import input.tar imageName:tag
Example: docker import ubuntu container.tar my-ubuntu-container:latest

These commands cover various aspects of working with Docker images, including pulling, listing, removing, tagging, building, inspecting, and managing images. Adjust these examples based on your specific use cases and requirements.

**Docker Container**

Docker containers are instances of Docker images, and they encapsulate applications and their dependencies, allowing them to run consistently across different environments. Here are some basic Docker container commands with examples:

1.  **Pulling an Image:** To download a Docker image from a registry (e.g., Docker Hub), you use the docker pull command. For example, to pull the official  

Nginx image:

docker pull nginx

2. **Running a Container:** To run a container from an image, you use the docker run command. For example, to start a basic Nginx web server:

docker run -d -p 8080:80 nginx

1.  \-d: Run the container in the background (detached mode).
    
2.  \-p 8080:80: Map port 8080 on the host to port 80 on the container.
    

3.  **Listing Running Containers:** To see the list of running containers, you use the docker ps command:
    
docker ps

4. **Stopping a Container:** To stop a running container, you use the docker stop command and specify the container ID or name:

docker stop

5.  **Starting a Stopped Container:** To start a stopped container:
    
docker start

6. **Removing a Container:** To remove a container, you use the docker rm command and specify the container ID or name:

docker rm

7. **Viewing Container Logs:** To view the logs of a running container:

docker logs

8.  **Executing Commands in a Running Container:** 

To execute a command inside a running container:
docker exec -it /bin/bash

This opens an interactive shell (bash) inside the container.

These are basic commands, and Docker provides many more options and features for managing containers.


