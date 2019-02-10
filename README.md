# pytest

# Build
Run build.sh script, which will generate a `build.tar` file.

# Installation
## Pre-requisites
Target VM should have docker and docker-compose pre-installed.Copy the generated `build.tar` to the target VM, and run the below steps:
1. `tar xvf buid.tar`
2. `cd installation`
3. `docker-compose up` - This will start a docker container with Python3 and also it would have copied all the required src files into the running container

# Verify
1. Login to the running container shell as : `docker exec -it <container id> /bin/bash`
2. `cd src`
3. `dos2unix main.sh main.sh;chmod +x main.sh`
4. Run the main script as : `main.sh input.csv`

