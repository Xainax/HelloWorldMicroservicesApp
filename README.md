# HelloWorldMicroservicesApp
## Project Description:
This application uses two Spring Boot projects, each being a microservice, that will communicate 
with each other to return the message "Hello World". Each microservice will be containerized in Docker 
and deployed on a Kubernetes cluster.

## Tools used to deploy application:
- Java + Spring Boot
- Docker
- Kubernetes
- Any IDE (I built this app using Visual Studio Code)

## Steps to install necessary tools: 
You will first need to download these tools to ensure the project builds correctly.
1. Download the code/clone this GitHub repository. 
2. Download Docker Desktop using the link https://docs.docker.com/get-started/get-docker/ and follow the steps for your operating system.
3. Download Kubernetes using the link https://kubernetes.io/releases/download/ and follow the steps for your operating system. 
4. Download Minikube using the link https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download#LoadBalancer and follow the steps for your operating system.
5. Download the correct version of Java. This project uses JDK 17 so any version above 17 should work as well. To check the version, you can run java -version in your terminal. 

For Windows, make sure that your JAVA_HOME and PATH environment variable is set to the correct Java installation path.
For Mac, you can edit your shell profile to change the JAVA_HOME and PATH environment variable are correct.

Once you cloned the repository, open the project in your IDE (I used Visual Studio Code).
Once you open the project, you can open the integrated terminal for the microservice as shown below.

Run ./gradlew build in both terminals.

Afterwards, run the command docker pull eric02pham/hello-service or eric02pham/world-service depending on which 
folder you are currently in. The docker image should show up in your Docker desktop. 

Now that you have downloaded the images, you can containerize them by pressing run button. For this project, change the 
port of hello-service to 8080 and the port for world-service to 8081.

After running the containers, go to your integrated terminal and run the command minikube start (keep in mind, if this is 
the first time you are running Minikube, it will take a bit of time)

After Minikube is installed and the cluster has been started, run the two following commands: minikube service hello-service and minikube service world-service. 



Links to Docker Images:
Hello Microservice: https://hub.docker.com/r/eric02pham/hello-service
World Microservice: https://hub.docker.com/r/eric02pham/world-service
