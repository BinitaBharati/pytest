#This is a sample Image 
#docker unbuntu image 
FROM ubuntu:16.04 
MAINTAINER binita.bharati@gmail.com 

RUN mkdir -p /root/dockerws/scripts/
RUN mkdir -p /root/dockerws/src/
WORKDIR /root/dockerws/

#Copy all the required files from host's file system to the container file system.
COPY scripts/install_python3.sh scripts/
COPY scripts/install_container.sh scripts/
COPY src/ src/

RUN apt-get update;apt-get -y install dos2unix
RUN apt-get install -y sqlite3

RUN dos2unix scripts/install_container.sh scripts/install_container.sh;chmod +x scripts/install_container.sh

ENTRYPOINT ["/root/dockerws/scripts/install_container.sh"]
