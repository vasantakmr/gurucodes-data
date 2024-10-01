---
title: "Docker Architecture"
---

## Docker uses a client-server architecture, consisting of the following components:

**Docker Client:**

*   The interface that users interact with.
    
*   It sends commands to the Docker daemon.
    

**Docker Daemon:**

*   The background service that manages Docker containers.
    
*   It receives commands from the Docker client and carries them out.
    

**Docker Images:**

*   Read-only templates that contain instructions for creating a container.
    
*   They are built from a Dockerfile, which specifies the steps to create the image.
    

**Docker Containers:**

*   Instances of a Docker image.
    
*   They are isolated environments that run applications.
    
*   Each container has its own file system, network, and process space.
    

**Docker Registry:**

*   A centralized repository for storing Docker images.
    
*   It allows users to share images with others.
    

**Docker Hub:**

*   A public Docker registry that is widely used.
    
*   It contains millions of images from various sources.
    

**Docker Compose:**

*   A tool for defining and running multi-container Docker applications.
    
*   It allows users to manage multiple containers as a single unit.
    

**Docker Swarm:**

*   A tool for clustering and orchestrating Docker containers.
    
*   It allows users to scale applications horizontally and manage multiple hosts.
    

**Docker Machine:**

*   A tool for provisioning Docker hosts on various platforms.
    
*   It allows users to create and manage Docker hosts on cloud platforms, virtual machines, and bare metal.
    

Docker uses a layered file system to optimize image storage and sharing. Each layer represents a change to the image. Layers are cached and reused, which can significantly improve image build times and reduce storage requirements.
