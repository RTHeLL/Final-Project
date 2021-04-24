# Final-Project
Requirements
-------------------------
[Docker](https://www.docker.com/ "Download and install latest version")


Install and Run/Stop
-------------------------
### Install
1. Clone project `git clone https://github.com/RTHeLL/Final-Project.git`
2. Build Docker image `docker build -t image-name .`
### Run/Stop
- Create and initial Start Docker container `docker run -d --name container-name -p 8000:8000 image-name`
- Start Docker container `docker start container-name`
- Stop Docker conatainer `docker stop container-name`
