---
title: "Core Components"
---

### 4.1 **Service Discovery**
In a microservices architecture, services need to find and communicate with each other dynamically. **Service discovery** mechanisms ensure that services register themselves when they are deployed and can be found by other services.
- Tools: **Consul**, **Eureka**, **Etcd**.

### 4.2 **API Gateway**
An **API Gateway** serves as a single point of entry for client requests. It routes requests to the appropriate services, handles authentication, rate limiting, and even response aggregation (combining data from multiple services).
- Tools: **Kong**, **Zuul**, **Traefik**.

### 4.3 **Load Balancing**
Distributes incoming network traffic across multiple services to ensure no single service is overwhelmed.
- Tools: **NGINX**, **HAProxy**, **Envoy**.

### 4.4 **Data Management**
In a monolith, you often have a single database. In microservices, each service typically has its own database, making them truly independent. This introduces the concept of **distributed data management**.
- Common approaches include **CQRS (Command Query Responsibility Segregation)** and **Event Sourcing** for handling distributed data consistency.

### 4.5 **Monitoring and Logging**
Since microservices are distributed across multiple instances, it's critical to have proper monitoring, logging, and tracing in place.
- Tools: **Prometheus**, **Grafana**, **ELK Stack**, **Jaeger** for distributed tracing.