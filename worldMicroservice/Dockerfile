FROM openjdk:17-jdk-slim
WORKDIR /app
COPY build/libs/demo-0.0.1-SNAPSHOT.jar worldService.jar
EXPOSE 8081
ENTRYPOINT ["java", "-jar", "worldService.jar"]