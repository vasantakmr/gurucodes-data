---
title: "kubernetes Ingress"
---

Ingress is a Kubernetes resource that lets external users access services in your cluster using clear routing rules. Think of Ingress as a gateway that decides how requests get to the right service in your application.

For example, if you have a multi-service app with separate frontend, backend, and API services, Ingress efficiently directs traffic to each service without needing multiple Load Balancers or NodePorts.

**Why Should You Use Ingress?**

Using Ingress comes with many advantages:

*   Unified Traffic Management: Manage traffic for multiple services from a single entry point.
    
*   Cost Efficiency: No need for separate Load Balancers for each service, which cuts down on cloud costs.
    
*   Flexible Routing: Use different routing methods, like URL or path-based routing, to fit your needs.
    
*   TLS/SSL Termination: Ingress can manage TLS certificates, keeping your traffic secure by encrypting it.
    

★   Key Advantages of Ingress

*   Centralized Access Control: Ingress provides one control point for managing access to various services in your cluster.
    
*   Scalability: Easily scale your applications without changing service-specific settings.
    
*   Enhanced Security: Supports HTTPS and TLS termination, ensuring your data is protected and communication is secure.
    

With these benefits, Ingress makes it easier to manage and secure your applications in Kubernetes!

**Real-Life Example**

Consider a scenario where you are deploying multiple **Flask** services: a **frontend**, **product service**, and **payment service**. Instead of creating separate load balancers for each, you can leverage **Ingress** to route traffic based on URL paths.

In this guide, we will:

*   Deploy three separate **Flask services**.
    
*   Create services to expose each one.
    
*   Use **Ingress** to route traffic accordingly.
    

**Step 1: Deploy Separate Flask Applications**

Let’s create three basic Flask apps: one for the **frontend**, one for the **product service**, and another for the **payment service**.

**Flask App for Frontend (frontend.py):**

```from flask import Flask
app = Flask(_name_)
@app.route('/') 
def home():

return "Hello, this is the frontend!"

if   name == "  main  ":

app.run(host='0.0.0.0', port=80)

**Flask App for Product Service (product.py):**

@app.route('/products') def products():

return "Welcome to the Product Service!"

if   name == "  main  ":

app.run(host='0.0.0.0', port=80)

**Flask App for Payment Service (payment.py):**

@app.route('/payments') def payments():

return "Welcome to the Payment Service!"

if   name == "  main  ":

app.run(host='0.0.0.0', port=80)

**Step 2: Create Docker Images for Each Flask App**

We will create **Docker images** for each of the Flask apps.

**Dockerfile** (can be the same for all three apps):

FROM python:3.8-slim WORKDIR /app

COPY . /app

RUN pip install flask

CMD \["python", "frontend.py"\] # Change filename to match the respective app: product.py or payment.py

Build and push the Docker images to your container registry:

**docker build -t /frontend:latest . docker push /frontend:latest**

**docker build -t /product:latest . docker push /product:latest**

**docker build -t /payment:latest . docker push /payment:latest**

**Step 3: Kubernetes Deployment for Flask Apps**

Now, let’s create Kubernetes deployment and service files for each Flask application.

**Frontend Deployment YAML:**

apiVersion: apps/v1 kind: Deployment metadata:

name: frontend-deployment

labels:

app: frontend-app spec:

replicas: 2

selector:

matchLabels:

app: frontend-app

template:

app: frontend-app

spec:

containers:

\- name: frontend-container

image: /frontend:latest

ports:

\- containerPort: 80

**Product Deployment YAML:**

apiVersion: apps/v1 kind: Deployment metadata:

name: product-deployment

labels:

app: product-app spec:

replicas: 2

selector:

matchLabels:

app: product-app

template:

app: product-app

spec:

containers:

\- name: product-container

image: /product:latest

ports:

\- containerPort: 80

**Payment Deployment YAML:**

apiVersion: apps/v1 kind: Deployment metadata:

name: payment-deployment

labels:

app: payment-app

spec:

replicas: 2

selector:

matchLabels:

app: payment-app

template:

app: payment-app

spec:

containers:

\- name: payment-container

image: /payment:latest

ports:

\- containerPort: 80

**Apply the Deployments:**

**kubectl apply -f frontend-deployment.yaml kubectl apply -f product-deployment.yaml kubectl apply -f payment-deployment.yaml**

**Step 4: Create Services for Each Flask App**

Now, let’s expose each of these deployments with **ClusterIP** services.

**Frontend Service YAML:**

apiVersion: v1 kind: Service metadata:

name: frontend-service spec:

selector:

app: frontend-app

ports:

\- protocol: TCP

port: 80

targetPort: 80

type: ClusterIP

**Product Service YAML:**

apiVersion: v1 kind: Service metadata:

name: product-service spec:

selector:

app: product-app

ports:

\- protocol: TCP

port: 80

targetPort: 80

type: ClusterIP

**Payment Service YAML:**

apiVersion: v1 kind: Service metadata:

name: payment-service spec:

selector:

app: payment-app

ports:

\- protocol: TCP

port: 80

targetPort: 80

type: ClusterIP

**Apply the Services:**

**kubectl apply -f frontend-service.yaml kubectl apply -f product-service.yaml kubectl apply -f payment-service.yaml**

**Step 5: Set Up Ingress Controller**

To manage external traffic, we need to install the **NGINX Ingress Controller**. This controller is essential as it routes incoming requests to the appropriate services based on the rules defined in our Ingress resource.

To manage external traffic, install the **NGINX Ingress Controller**.

**kubectl apply -f** **https://raw.githubusercontent.com/kubernetes/ingress-** **nginx/main/deploy/static/provider/cloud/deploy.yaml**

Verify that the **Ingress Controller** is running:

**kubectl get pods -n ingress-nginx**

**Step 6: Create Ingress Resource**

Now, let’s define an **Ingress** resource to route traffic to the appropriate service based on the URL path.

**Ingress YAML:**

apiVersion: networking.k8s.io/v1

kind: Ingress metadata:

name: flask-ingress spec:

ingressClassName: nginx

rules:

\- host: example.com

http:

paths:

\- path: /

pathType: Prefix

backend:

service:

name: frontend-service

port:

number: 80

\- path: /products

pathType: Prefix

backend:

service:

name: product-service

port:

number: 80

\- path: /payments

pathType: Prefix

backend:

service:

name: payment-service

port:

number: 80

**Note:** **ingressClassName**: Specifies the Ingress class that this resource belongs to (e.g., nginx). This tells Kubernetes which Ingress controller to use for this resource. If omitted, the default Ingress controller will be used.

This Ingress resource outlines routing rules:

*   / directs traffic to the **frontend service**.
    
*   /products routes traffic to the **product service**.
    
*   /payments routes traffic to the **payment service**.
    

 •? ¸Ç **Validating Your Ingress**

After setting up your Ingress resource, you can validate that it's working correctly.

1.  **Check Ingress Status: kubectl get ingress**
    

This command should display the Ingress resource you created, along with its associated rules.

1.  **Test the Ingress Using Curl:** Use the following commands to test the routing:
    

**curl -H "Host: example.com" http:///**

**curl -H "Host: example.com" http:///products curl -H "Host: example.com"** **http:///payments**

**Sample Output**

*   **For the frontend:**
    

**Hello, this is the frontend!**

*   **For the product service: Welcome to the Product Service!**
    
*   **For the payment service: Welcome to the Payment Service!**
