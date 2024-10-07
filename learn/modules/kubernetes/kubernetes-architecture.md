---
title: "kubernetes Architecture"
---
**Container Orchestration**


*   **Definition**: Automates deployment, management, scaling, and networking of containers across a cluster.
    
*   **Focus**: Manages the lifecycle of containers.
    
*   **Use Case**: Useful for enterprises needing to manage hundreds or thousands of containers and hosts.

**Automated Tasks:**

1.  Configuring and scheduling containers.
    
2.  Provisioning and deploying containers.
    
3.  Ensuring redundancy and availability.
    
4.  Scaling containers up or down based on application load.
    
5.  Moving containers if a host has insufficient resources or fails.
    
6.  Allocating resources between containers.
    
7.  Exposing services to the outside world.
    
8.  Load balancing between containers.
    
9.  Health monitoring of containers and hosts.
    

**What is Kubernetes (K8s)?**

*   **Definition**: Kubernetes is an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications. It was originally developed by Google and is now maintained by the Cloud Native Computing Foundation (CNCF).
    
*   **Purpose**: It helps manage clusters of containers at scale, enabling high availability, scalability, and ease of deployment for applications.

**Why Do We Use Kubernetes?**

*   **Container Orchestration**: Manages the lifecycle of containers, ensuring they are running and can scale based on demand.
    
*   **High Availability**: Provides self-healing capabilities, automatically restarting, rescheduling, or replacing containers that fail or are terminated.
    
*   **Scalability**: Easily scales applications up or down based on traffic or resource needs.
    
*   **Automated Deployment and Rollbacks**: Allows automated rollouts and rollbacks of applications, making continuous integration and delivery easier.
    
*   **Resource Optimization**: Efficiently manages resources such as CPU and memory, ensuring optimal utilization.

**Use Cases of Kubernetes**

*   **Microservices Architecture**: Running and managing microservices applications that need isolated environments but want to communicate effectively.
    
*   **CI/CD Pipelines**: Automating the deployment process for continuous integration and delivery.
    
*   **Hybrid Cloud and Multi-Cloud Deployments**: Managing workloads across different cloud providers or on-premises infrastructure.
    
*   **Big Data and Machine Learning**: Orchestrating workloads like big data processing or machine learning models that require significant computational power.

**Features of Kubernetes**

*   **Automated Bin Packing**: Automatically places containers based on their resource requirements and constraints.
    
*   **Service Discovery and Load Balancing**: Automatically assigns IP addresses and a single DNS name for a set of containers, along with load balancing.
    
*   **Storage Orchestration**: Mounts and manages storage systems like local storage, public cloud providers, and more.
    
*   **Self-Healing**: Restarts failed containers, replaces and reschedules them, and kills those that don’t respond to user-defined health checks.
    
*   **Horizontal Scaling**: Automatically scales applications up or down based on CPU utilization or custom metrics.
    
*   **Automated Rollouts and Rollbacks**: Deploys changes to the application or configuration and roll back to a previous state if needed.
    
*   **Secret and Configuration Management**: Stores and manages sensitive information like passwords, OAuth tokens, and SSH keys.

**Kubernetes architecture overview**

*   K8 nodes are divided into 2 types, master node(control plane), and worker node
    
*   These nodes can be a physical machines as well as the virtual machines
    
*   Master and Worker nodes have different components resided inside it
    
**Master Node (Control Plane) components**

*   API Server
    
*   ETCD
    
*   Control Manager
    
*   Scheduler

**Worker Node Components**

*   Kubelet
    
*   kube-proxy

**Kubernetes Master server components**

### **API Server**

*   It basically redirects all the API to a particular component, for example, if we wish to create a pod, then our request is received by the API server, and then it will forward it to the control manager.
    
*   End-user only will talk to API server only.
    
*   The API server will also authenticate and authorize the user
    
*   Masters communicate with the rest of the cluster through the kube-apiserver, the main access point to the control plane.
    
*   It validates and executes user's REST commands
    
*   kube-apiserver also makes sure that configurations in etcd match with configurations of containers deployed in the cluster
    
*   The front-end for the Kubernetes control plane. It exposes the Kubernetes API and acts as the gateway to the cluster.

### **Etcd**

*   ETCD is a distributed reliable key-value store used by Kubernetes to store all data used to manage the cluster.
    
*   It is a database for k8, data is stored in the form of key-value pair.
    
*   it has data of nodes, config, secret, accounts, role binding, replica set, replica controller, RBAC, etc.
    
*   When you have multiple nodes and multiple masters in your cluster, etcd stores all that information on all the nodes in the cluster in a distributed manner.
    
*   ETCD is responsible for implementing locks within the cluster to ensure there are no conflicts between the Masters
    
*   A key-value store used for storing all cluster data, maintaining the state of the cluster.

### **Control Manager**

*   The controllers are the brain behind orchestration.
    
*   They are responsible for noticing and responding when nodes, containers or endpoints goes down.
    
*   The controllers makes decisions to bring up new containers in such cases.
    
*   The kube-controller-manager runs control loops that manage the state of the cluster by checking if the required deployments, replicas, and nodes are running in the cluster
    
*   Manages various controllers, ensuring the desired state of the cluster is maintained. This includes node controllers, replication controllers, and more.

### **Node Controller**

*   it will check for the number of workers in the k8 cluster is available for not.
    
*   It will check for node state every 5 seconds, if any of the nodes will not respond for 40 seconds then node schedular will mark it as unreachable.
    
*   After that, if that node still does not respond in the next 5 minutes, then k8 will schedule the pod present in that node to some other node
    

### **Scheduler**

*   Scheduler task is to schedule the tasks(like creating pod) on the proper node, it checks for the highest ram and storage available node and schedules the tasks accordingly, it basically manages the load between the nodes.
    
*   It looks for newly created containers and assigns them to Nodes.
    
*   Assigns work to the worker nodes based on resource availability and other constraints. It decides where a new Pod should be placed.

**Kubernetes Worker node components**

### **kubelet**
*   Worker nodes have the kubelet agent that is responsible for interacting with the master to provide health information of the worker node
    
*   To carry out actions requested by the master on the worker nodes.
    
*   Kublet's task is to create the pod and monitor its status and provide the report to the API server.
    
*   It will only manage containers which are created by k8 only
    
*   An agent that runs on each worker node, ensuring the containers are running in a Pod as expected. It communicates with the master components.

### **Kube-proxy**

*   Kube proxy will create and manage the network rules, it will help to establish communication between two pods which are in different nodes
    
*   The kube-proxy is responsible for ensuring network traffic is routed properly to internal and external services as required and is based on the rules defined by network policies in kube-controller-manager and other custom controllers.
    
*   Maintains network rules and handles communication between services in the cluster. It ensures the correct routing of traffic to the right containers.

**Container Runtime**: The software responsible for running containers (e.g., Docker, containerd, CRI-O).

### **What is Kubectl**

*   kubectl is the command line utility using which we can interact with k8s cluster
    
*   Uses APIs provided by API server to interact.
    
*   Also known as the kube command line tool or kubectl or kube control.
    
*   Used to deploy and manage applications on a Kubernetes