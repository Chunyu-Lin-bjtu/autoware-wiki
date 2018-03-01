This page guides you to install and run Autoware on the NVIDIA DRIVE PX2 platform using Docker. Note that DRIVE PX2 requires you to be a licensee of NVIDIA DRIVE and DevZone. To complete the installation process introduced below, please contact Autoware Developers Group at autoware@googlegroups.com, and you will get more information on Autoware Docker for DRIVE PX2. For other platforms, such as Generic x86, please check [here](https://github.com/CPFL/Autoware/wiki/Docker) whether they are supported. The outline of this page is as follows:

1. Docker Setup
1. Autoware Setup

## Docker Setup
### Docker Package Installation
   You first need to build the Docker environment. You may not access docker.io with the default configuration of Ubuntu 16.04, so try the following installation process.
   ```bash
   $sudo apt-get install -y software-properties-common
   $sudo apt-add-repository universe
   $sudo apt-get update
   $sudo apt-get install docker.io
   $sudo apt-get update
   ```

### Docker Package Test
   Type the following commands.
   ```bash
   $sudo docker info | grep "Docker Root Dir"
   ``` 
   Everything should be ready if you find the following description.
   ```bash
   Docker Root Dir: /var/lib/docker
   ``` 

## Autoware Setup

### Requirements
- 15 GB of free space (7GB temporarily used)
- CUDA9.0 installed

### Docker Image Installation
Download [install_autoware_drivepx2_docker.sh](https://github.com/CPFL/Autoware/blob/master/docker/nvidia/install_autoware_drivepx2_docker.sh) to your favorite directory, and change the current directory.

   ```bash
   $ sudo ./install_autoware_drivepx2_docker.sh
   $ source ~/.bashrc
   ```

If you use another shell, please add "/usr/local/autoware/bin" to ${PATH}.

### How To Run
`$ autoware-docker`

You should be now in the Autoware Docker container. To launch Autoware, run:

`$ ~/start_autoware.sh`
 
Autoware should be now running successfully.

### How Autoware and DriveWorks Interact
![flow_gmsl](https://raw.githubusercontent.com/CPFL/Autoware/master/docker/nvidia/docs/autoware_driveworks_overview.png)
![flow_gmsl](https://raw.githubusercontent.com/CPFL/Autoware/master/docker/nvidia/docs/flow_gmsl.png)
![flow_tensorrt](https://raw.githubusercontent.com/CPFL/Autoware/master/docker/nvidia/docs/flow_tensorrt.png)