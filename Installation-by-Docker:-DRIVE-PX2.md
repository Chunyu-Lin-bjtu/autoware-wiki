# Overview
This page guides you to install and run Autoware on the NVIDIA DRIVE PX2 platform using Docker. Note that DRIVE PX2 requires you to be a licensee of NVIDIA DRIVE and DevZone. To complete the installation process introduced below, please contact Autoware Developers Group at autoware@googlegroups.com, and you will get more information on Autoware Docker for DRIVE PX2. If you are looking for the generic x86 Docker, please visit [here](https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-Generic-x86).

# Outline
* Docker Setup
* Autoware Setup

# Docker Setup
## Docker Package Installation
   You first need to build the Docker environment. You may not access docker.io with the default configuration of Ubuntu 16.04, so try the following installation process.
   ```bash
   $sudo apt-get install -y software-properties-common
   $sudo apt-add-repository universe
   $sudo apt-get update
   $sudo apt-get install docker.io
   $sudo apt-get update
   ```

## Docker Package Test
   Type the following commands.
   ```bash
   $sudo docker info | grep "Docker Root Dir"
   ``` 
   Everything should be ready if you find the following description.
   ```bash
   Docker Root Dir: /var/lib/docker
   ``` 

# Autoware Setup
Please first contact Autoware Developers Group at autoware@googlegroups.com to get the script files for your favorite configuration (see Case 1 and Case 2 below).

## Case 1: Autoware with NVIDIA DriveWorks
### Step 1: Run Setup Script.
Run setup_with_driveworks.sh that you obtained.  
Use apt-get as follows if you cannot find the curl command.
   ```bash
   $ sudo apt-get install curl
   ``` 
### Step 2: Run Installation Script.
Run install_with_driveworks.sh that you obtained.
## Case 2: Autoware without NVIDIA DriveWorks
### Step 1: Run Setup Script.
Run setup_without_driveworks.sh that you obtained.  
Use apt-get as follows if you cannot find the curl command.

### Step 2: Run Installation Script.
Run install_without_driveworks.sh that you obtained.

## Autoware Test
You should face xterm after running the installation script. Please finally run start_autoware.sh that is located in the current directory.
   ```bash
   $ ./start_autoware.sh
   ``` 
Autoware should be now running successfully.

***

[[Home](https://github.com/CPFL/Autoware/wiki/)]
