This page guides you to install and run Autoware on the Syn Quacer E using Docker.

1. Docker Setup
1. Autoware Docker Setup

## Docker Setup

You first need to build the Docker environment. If the following installation process does not work for you, please check [Docker's installation website](https://docs.docker.com/install/linux/docker-ce/debian/).

### Old Docker Cleanup
```
$ sudo apt-get remove docker docker-engine docker.io
```

You are ready to move on the next step if all Docker packages are removed.

### Docker CE Installation
This time you may want to install Docker using the repository, though there are several other ways to install Docker.

#### Step 1: Repository Setup
Do update on apt-get.
```
$ sudo apt-get update
```

Permit apt-get to access the repository.
```
$ sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

Add Docker's official GPG key docker.
```
$ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

Validate the key. If you see the fingerprint below, you are reay to move on the next step.
```
$ sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```

Install the repository.
```
$ echo "deb [arch=armhf] https://download.docker.com/linux/debian \
     $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list
```

#### Step 2: Docker CE Installation
Update on apt-get.
```
$ sudo apt-get update
```

Install the latest version of Docker CE.
```
$ sudo apt-get install docker-ce
```

Validate the installation succeeded.
```
$ sudo docker run armhf/hello-world
```

## Autoware Docker Setup
You can build the Autoware runtime environment using docker. You may choose either to use the configuration of Docker Hub "as is" or to modify-then-recompile Dockerfile.

### Case 1: Using Docker Hub "As Is"
Move to the docker/96boards directory in Autoware.
```
$ git clone https://github.com/CPFL/Autoware.git
$ cd Autoware/docker/96boards
```

Coming soon.