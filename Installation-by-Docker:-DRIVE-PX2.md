# Overview
This page guides you to install and run Autoware on the NVIDIA DRIVE PX2 platform using Docker. Note that DRIVE PX2 requires you to be a licensee of NVIDIA DevZone. To complete the installation process introduced below, please contact Autoware Developers Group at autoware@googlegroups.com, and you will get more information on Autoware Docker for DRIVE PX2.

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










