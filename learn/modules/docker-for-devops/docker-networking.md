---
title: "docker networking"
---

**Docker Network**

Docker provides a networking feature that allows containers to communicate with each other and with the outside world. Docker networking enables seamless connectivity between containers on the same host or across multiple hosts in a cluster. Here's an overview of Docker networking concepts along with examples:

**Docker Networking Concepts:**

1.  **Bridge Network:**
    
The default network type for containers.Containers on the same bridge network can communicate with each other.Each container gets its own IP address within the bridge network.
    
2.  **Host Network:**

Containers share the host's network stack.Containers can directly bind to host ports.
    
3.  **Overlay Network:**
    
Used for connecting containers across multiple Docker hosts (in a swarm cluster).It Provides network abstraction, allowing containers to communicate as if they are on the same host.Commonly used in Docker Swarm mode.

4.  **User-Defined Bridge Network:**
    
Custom bridge networks can be created by users.The Containers on the same custom bridge network can communicate with each other.
    
**Docker Network Commands:**

1.  **Create a Custom Bridge Network:**
docker network create mynetwork

2.  **Run a Container on a Specific Network:**
docker run --network mynetwork --name mycontainer -d nginx

3.  **Inspect Network Details:**
docker network inspect mynetwork

4.  **Connect a Container to a Network:**
docker network connect mynetwork mycontainer

5.  **Disconnect a Container from a Network:**
docker network disconnect mynetwork mycontainer

6.  **List Networks:**  
docker network ls

**Example: Custom Bridge Network**

1.  **Create a Custom Bridge Network:**
docker network create mynetwork

2.  **Run Containers on the Custom Network:**   
docker run --network mynetwork --name container1 -d nginx
docker run --network mynetwork --name container2 -d nginx

3.  **Inspect Network Details:**
docker network inspect mynetwork

Look for the containers under the "Containers" section.

4.  **Communication Between**

**Containers:** Containers container1 and container2 can communicate with each other using their container names as hostnames.

Docker networking is a powerful feature that facilitates communication between containers, and it becomes especially crucial in scenarios where you have multiple containers or services working together.