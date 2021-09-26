FROM openjdk:17-alpine
COPY /servidor3 /root/minecraft
WORKDIR /root/minecraft
EXPOSE 25575
CMD java -Xmx1024M -Xms1024M -jar server.jar nogui


