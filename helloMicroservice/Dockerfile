FROM openjdk:17-jdk-slim
WORKDIR /app
COPY build/libs/demo-0.0.1-SNAPSHOT.jar helloService.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "helloService.jar"]