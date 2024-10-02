---
title: "Integration of Tools: Drive the Jenkins Train"
---


**1. Project Overview**

This project demonstrates a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub for source control, Jenkins for automation, and Docker Hub for container images, and a Linux server for deployment. The goal is to automate the process of building, testing, and deploying a Docker image to a Linux server whenever changes are pushed to the GitHub repository.

**2. Prerequisites**

*   A GitHub account
    
*   A Jenkins server
    
*   A Docker Hub account
    
*   A Linux server with Docker installed
    
*   Basic understanding of Docker, Jenkins, and Linux commands
    

**3. Setting Up GitHub Repository**

1.  Create a GitHub Repository:
    
    *   Go to GitHub and create a new repository.
        

*   Clone the repository to your local machine.
    

```sh

git clone https://github.com/yourusername/your-repo.git

cd your-repo

```

2.  Add Your Project Files:
    

*   Create a basic application, for example, a simple Node.js app or a static website.
    

- Create a `Dockerfile` to containerize your application.

```dockerfile

FROM node:14

WORKDIR /app

COPY . .

RUN npm install

CMD ["node", "app.js"]

```

3.  Push to GitHub:
    

- Add, commit, and push your files to the GitHub repository.

```sh

git add .

git commit -m "Initial commit"

git push origin main

```

4. **Setting Up Jenkins**

1.  Install Jenkins:
    

*   Follow the [official Jenkins installation guide](https://www.jenkins.io/doc/book/installing/) for your platform.
    

2.  Configure Jenkins:
    
    *   Install the necessary plugins:
        
*   Git Plugin
    
*   Docker Pipeline Plugin
    

*   Create a new Jenkins job (Pipeline):
    
*   Go to Jenkins dashboard, click on "New Item".
    
*   Enter a name for the job, select "Pipeline", and click "OK".
    

3.  **Docker Hub Configuration**
    

1.  Create a Repository on Docker Hub:
    

*   Go to Docker Hub and create a new repository.
    

4.  Generate Access Token:
    

*   In Docker Hub, go to "Account Settings" > "Security" > "New Access Token".
    
*   Save the token securely.
    

5. **Jenkins Pipeline Configuration**

1.  Pipeline Script:
    

*   Configure your Jenkins job with the following pipeline script.
    
```groovy

pipeline {

agent any

environment {

DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')

REPO = 'yourdockerhubusername/your-repo'

}

stages {

stage('Clone Repository') {

steps {

git 'https://github.com/yourusername/your-repo.git'

}

}

stage('Build Docker Image') {

steps {

script {

dockerImage = docker.build("${env.REPO}:${env.BUILD_ID}")

}

}

}

stage('Push Docker Image') {

steps {

script {

docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') { dockerImage.push("${env.BUILD_ID}") dockerImage.push("latest")

}

}

}

}

stage('Deploy to Linux Server') {

steps {

sshagent(['your-ssh-credentials-id']) {

sh '''

ssh youruser@yourserver "docker pull ${env.REPO}:latest && docker stop myapp || true && docker rm myapp || true && docker run -d --name myapp -p 80:80 ${env.REPO}:latest"

'''

}

}

}

}

post {

always {

cleanWs()

}

}

}

```

1.  Credentials Setup:

*   In Jenkins, go to "Manage Jenkins" > "Manage Credentials" and add:
    

*   Docker Hub credentials (`dockerhub-credentials-id`).
    

*   SSH credentials for your Linux server (`your-ssh-credentials-id`).
    

**7. Deploying to the Linux Server**

1.  Ensure Docker is Installed:
    
- Make sure Docker is installed and running on your Linux

server.

```sh

sudo apt-get update

sudo apt-get install -y docker.io

sudo systemctl start docker

sudo systemctl enable docker

```

1.  Setup SSH Access:
    
*   Ensure that your Jenkins server can SSH into your Linux server without a password prompt.
    
8. **Testing and Verification**

1.  Trigger a Build:
    
*   Push a change to your GitHub repository to trigger the Jenkins pipeline.
    

```sh

git commit -m "Trigger build"

git push origin main

```

1.  Check Jenkins:

*   Monitor the Jenkins job to ensure all stages pass successfully.
    
1.  Verify Deployment:
    
*   Access your application on the Linux server to confirm it’s running as expected.
    

9. **Conclusion**

This documentation provides a detailed guide on setting up a CI/CD pipeline using GitHub, Jenkins, and Docker Hub. By following these steps, you can automate the process of building, testing, and deploying your application, ensuring a streamlined workflow.