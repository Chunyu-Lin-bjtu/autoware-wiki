*Under construction.*

This page guides you to install and run Autoware on the SynQuacer E using Docker. The outline of this page is as follows.

1. Debian Setup
1. Docker Setup
1. Autoware Docker Setup

## Attention

* The performance is not optimized for SynQuacer E.
* Yolo2 is not built.
* Checkout develop branch for Docker scripts.
* Indigo is not supported now ([#1356](https://github.com/CPFL/Autoware/pull/1356)).

## Debian Setup

You first install Debian according to [SynQuacer(TM) E-Series Assembly Instructions](http://www.socionext.com/en/download/catalog/MN04-00002-2E.pdf).

## Docker Setup

You need to build the Docker environment. If the following installation process does not work for you, please check [Docker's installation website](https://docs.docker.com/install/linux/docker-ce/debian/).

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
$ echo "deb [arch=armhf] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
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
$ cd Autoware
$ git checkout develop
$ cd docker/96boards
```

Modify the last sentence of run.sh in that directory: autoware-$1 --> autoware/autoware:1.7.0-kinetic-96boards (*comment out does not work, need to modify)

Run run.sh kinetic, assuming that the default path is "/home/$USER/shared_dir".
```
$ sudo sh run.sh kinetic
```

If you want to use your own path, run build.sh kinetic with the path argument.
```
$ sudo sh run.sh kinetic {SHARED_DIR_PATH}
```

### Case 2: Using modify-then-recompile Dockerfile
#### Step 1: Autoware Docker Build

Move to the docker directory in Autoware.
```
$ git clone https://github.com/CPFL/Autoware.git
$ cd Autoware
$ git checkout develop
$ cd docker/96boards
```

Run build.sh kinetic.
```
$ sudo sh build.sh kinetic
```

#### Step2: Autoware Docker Run

Run run.sh kinetic, assuming that the default path is "/home/$USER/shared_dir".
```
$ sudo sh run.sh kinetic
```

If you want to use your own path, run build.sh kinetic with the path argument.
```
$ sudo sh run.sh kinetic {SHARED_DIR_PATH}
```