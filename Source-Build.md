### Requirements

- ROS kinetic (Ubuntu 16.04)
- OpenCV 2.4.10 or higher
- Qt 5.2.1 or higher
- CUDA (optional)
- FlyCapture2 (optional)
- Armadillo (optional)

**Please use Autoware v1.9.1 if you want to use ROS indigo.**

### Install system dependencies for Ubuntu 14.04 Indigo

```
% sudo apt-get install -y  python-catkin-pkg python-rosdep python-wstool ros-$ROS_DISTRO-catkin
% sudo add-apt-repository ppa:mosquitto-dev/mosquitto-ppa
% sudo apt-get update
% sudo apt-get install libmosquitto-dev
```

**NOTE: Please do not install ros-indigo-velodyne-pointcloud package. If it is already installed, please uninstall.**

### Install system dependencies for Ubuntu 16.04 Kinetic
```
% sudo apt-get update
% sudo apt-get install -y python-catkin-pkg python-rosdep python-wstool ros-$ROS_DISTRO-catkin libmosquitto-dev gksu
```

**NOTE: Following packages are not supported in ROS Kinetic.**
- gazebo
- orb slam
- dpm ocv

### How to build

1. Clone the repository

```
$ cd $HOME
$ git clone https://github.com/CPFL/Autoware.git --recurse-submodules
```
or if you already have a copy of the repo, run `$ git submodule update --init --recursive`.

2. Initialize the workspace, let rosdep to install the missing dependencies and compile.

#### Build with catkin

```
$ cd ~/Autoware/ros/src
$ catkin_init_workspace
$ cd ../
$ rosdep update
$ rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO
$ ./catkin_make_release
```
### Build using colcon

Install colcon, and its dependencies:
```
$ sudo apt-get install -y python3-pip python3-setuptools
$ sudo pip3 install -U setuptools
$ sudo apt-get install -y python3-colcon-common-extensions
```

Compile 
```
$ cd ~/Autoware/ros/src
$ rosdep update
$ rosdep install -y --from-paths src --ignore-src --rosdistro $ROS_DISTRO
$ ./colcon_release

```

### DNN-based nodes

Several DNN-based nodes, such as RCNN, SSD, and Yolo, are not automatically built.

To build these nodes please follow the respective node's README
[SSD](https://github.com/CPFL/Autoware/tree/master/ros/src/computing/perception/detection/vision_detector/packages/vision_ssd_detect/README.md)
**Darknet** is now included in Autoware perception.


Also be careful when changing files under `ros/src/sensing/drivers/lidar/packages/velodyne`. There is **subtree**.
The original repository is [here](https://github.com/CPFL/velodyne). If you change those files from this
repository, you must use **git subtree push**. (Please never change and push code if you don't understand
`git subtree` well).

### How to start

```
$ cd $HOME/Autoware/ros
$ ./run
```