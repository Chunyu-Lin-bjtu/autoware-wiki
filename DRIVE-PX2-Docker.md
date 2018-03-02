This page guides you to install and run Autoware on the NVIDIA DRIVE PX2 platform using Docker. **Note that DRIVE PX2 requires you to be a licensee of NVIDIA DRIVE and DevZone**. To complete the installation process introduced below, please contact Autoware Developers Group at autoware@googlegroups.com. For other platforms, such as Generic x86, please check [here](https://github.com/CPFL/Autoware/wiki/Docker) whether they are supported. The outline of this page is as follows:

1. Docker Setup
1. Autoware Setup
1. DriveWorks Interface

## Docker Setup
### Docker Package Installation
   You first need to setup the Docker environment. You may not access docker.io with the default configuration of Ubuntu 16.04, so try the following installation process.
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
   If you get the following output, you might continue with the process.
   ```bash
   Docker Root Dir: /var/lib/docker
   ``` 

## Autoware Setup

### Requirements
- 15 GB of free space (7GB temporarily used)
- CUDA 9.0 installed

### Docker Image Installation
* Download [install_autoware_drivepx2_docker.sh](https://github.com/CPFL/Autoware/blob/master/docker/nvidia/install_autoware_drivepx2_docker.sh).
* Change to the download directory, and execute the following commands in the terminal. *Note that the script will modify `.bashrc` to add Autoware to the path env variable. If you a different shell than bash, please add "/usr/local/autoware/bin" to `${PATH}`.*

   ```bash
   $ sudo ./install_autoware_drivepx2_docker.sh
   $ source ~/.bashrc
   ```

### How to Run
Execute

`$ autoware-docker`

This will launch an interactive bash inside the Docker container. To launch Autoware, run:

`$ ~/start_autoware.sh`
 
Autoware RTM should be displayed.

## DriveWorks Interface

Autoware integrates a ROS interface to communicate with the DriveWorks API. This interface is provided as the *autoware_driveworks_interface* package, where the actual codebase is protected by the binary format due to a proprietary constraint of DriveWorks. When using DriveWorks with Autoware, we encourage you to use the DriveWorks Sensor Abstraction Layer (SAL), which provides a universal interface for different sensors, such as LiDARs and cameras, to be efficiently managed on the DRIVE PX2 platform.

![flow_gmsl](https://raw.githubusercontent.com/CPFL/Autoware/master/docker/nvidia/docs/autoware_driveworks_overview.png)

### Basic Flow of Image Sensing with GMSL Cameras 
![flow_gmsl](https://raw.githubusercontent.com/CPFL/Autoware/master/docker/nvidia/docs/flow_gmsl.png)

### Basic Flow of Image Recognition with TensorRT
![flow_tensorrt](https://raw.githubusercontent.com/CPFL/Autoware/master/docker/nvidia/docs/flow_tensorrt.png)