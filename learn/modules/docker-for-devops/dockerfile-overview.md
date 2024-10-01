---
title: "Dockerfile Setup"
---
**Dockerfile**

A Dockerfile is a script that contains instructions for building a Docker image. It specifies the base image, sets up the environment, installs dependencies, and defines how the application should run. Let's go through the key components of a Dockerfile using a simple example.

**Example Dockerfile:**

*   Use an official Python runtime as a parent image 

FROM python:3.8-slim
    

*   Set the working directory in the container 

WORKDIR /app
    

*   Copy the current directory contents into the container at /app 

COPY . /app
    

*   Install any needed packages specified in requirements.txt
    

RUN pip install --no-cache-dir -r requirements.txt

*   Make port 80 available to the world outside this container 

EXPOSE 80
    

*   Define environment variable
    
ENV NAME World

*   Run app.py when the container launches 

CMD ["python", "app.py"]
    

**Explanation:**

1.  **FROM:**
    
Specifies the base image for the Docker image. In this case, it uses the official Python 3.8 image as a starting point.
    
2.  **WORKDIR:**
    
Sets the working directory inside the container to /app. Subsequent instructions will be executed in this directory.
    
3.  **COPY:**
    
Copies the current directory (the directory where the Dockerfile is located) into the container at /app. This includes your application code.
    
4.  **RUN:**
    
Executes commands in the container during the build process. In this example, it installs the Python dependencies specified in requirements.txt.
    
5.  **EXPOSE:**
    
Informs Docker that the container will listen on the specified network ports at runtime. It does not actually publish the ports; it's more of a documentation feature.
    
6.  **ENV:**
    
Sets an environment variable, in this case, NAME with the value "World". This variable can be accessed by the application inside the container.
    
7.  **CMD:**
    
Provides the default command to run when the container starts. In this example, it runs python app.py. You can override this command when running the container.
    
**Usage:**

1.  Save the above Dockerfile in a file named Dockerfile in your project directory.
    
2.  Create a file named requirements.txt if your application has Python dependencies. Add the necessary dependencies.

3.  Create your Python application file (e.g., app.py) in the same directory.
    
4.  Build the Docker image:

docker build -t my-python-app .

5.  Run the Docker container:

docker run -p 4000:80 my-python-app

This example assumes a simple Python web application. Adjust the Dockerfile based on your specific application, its dependencies, and how it needs to be executed within the container.