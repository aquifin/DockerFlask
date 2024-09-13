# Building a RESTful API with Python Flask : A Comprehensive Guide
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" height="50"/> <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" alt="Flask" height="50"/> 


---

### Features
- **List Students**: Retrieve a list of all available students.
- **Add Student**: Add a new student to the collection.
- **Delete Student**: Remove a student from the collection.



-  run the application by using the following command in the terminal.
    ```shell
    python app.py
    ```

-  Open your browser and navigate to http://localhost:5000. You should see the page and be able to interact with the APIs.

---
# Dockerizing a Python Flask App: A Step-by-Step Guide to Containerizing Your Web Application
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" height="50"/> <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" alt="Flask" height="50"/> <img src="https://upload.wikimedia.org/wikipedia/en/f/f4/Docker_logo.svg" alt="Docker" height="50"/>

Discover the essentials of containerizing your Python Flask app with Docker. This guide covers creating Dockerfiles, optimizing builds, and using Docker Compose for deployment. Follow step-by-step instructions to encapsulate your app, manage dependencies, and ensure consistency. Whether you're new to Docker or enhancing your skills, unlock containerization's power and elevate your development workflow.

---

1.  Install Docker
    - Refer to this like [https://www.docker.com/get-started/](https://www.docker.com/get-started/) to install Docker on your machine.
2.  Create a Python Flask project
    
3. Create `Dockerfile` in the root of the project.
   
4. Build a `Docker Image`
   ```bash
   docker build -t api-flask .
   ```
   If you run the following command, you will see the created `Docker Image`.
   ```bash
   docker images
   ```
   ```
    REPOSITORY                   TAG               IMAGE ID       CREATED          SIZE
    api-flask                    latest            161bac35dd39   11 seconds ago   183MB
   ```
   *Some values may be different.*

5. Start a `Docker container`
   ```bash
   docker run -p 5000:5000 --name api-flask-container -d api-flask
   ```
   
6. Open your browser and navigate to http://localhost:5000. You should see the page and be able to interact with the APIs.
   
7. Open a new terminal and run the following command, you will see the created `Docker Container`.
   ```bash
    docker ps
   ```
   ```
    CONTAINER ID   IMAGE                             COMMAND                  CREATED              STATUS              PORTS                    NAMES
    4d355b2637dd   api-flask                         "gunicorn applicatio…"   About a minute ago   Up About a minute   0.0.0.0:8080->5000/tcp   api-flask-container
   ```
   *Some values may be different.*

   ---

   ## Tips   
    1. To remove a Docker image:
        ```bash
        docker rmi <image_name_or_id>
        ```
    2. To remove all the Docker images:
        ```bash
        sudo docker rmi $(docker images -q)
        ```
    3. To stop a Docker container:
        ```bash
        docker stop <container_name_or_id>
        ```
    4. To remove a Docker container:
        ```bash
        docker rm <container_name_or_id>
        ```
    5. To remove all the stopped Docker containers:
        ```bash
        docker container prune
        ```
    6. To remove all the Docker containers:
        ```bash
        sudo docker rm $(docker ps -a -q)
        ```
    7. To save a Docker image in your machine:
        ```bash
        docker save -o api-flask.tar api-flask
        ```
    8. To load a Docker image:
        ```bash
        docker load -i api-flask.tar
        ```
    9. To push a Docker image to the Docker Hub:
        ```bash
        docker login

        # amd64
        docker buildx build --platform linux/amd64 -t <your_docker_hub_username>/api-flask:latest-amd64 --push .
        
        # arm64
        docker buildx build --platform linux/arm64 -t <your_docker_hub_username>/api-flask:latest-arm64 --push .
        ```

