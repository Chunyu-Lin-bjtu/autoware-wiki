To install Autoware, we strongly recommend using our Docker environments. The supported version of Autoware is newer than 1.6.0. In case that you do not want to use Docker for installation, please follow the instruction provided by [Source Build](https://github.com/CPFL/Autoware/wiki/Source-Build).

## Generic x86 (64 bits)

The preferred computing environments are listed as follows:

* Intel Core i7 (preferred), Core i5, Atom
* 16GB to 32GB of main memory
* More than 30GB of SSD
* NVIDIA GTX GeForce GPU (980M or higher performance)

[>> Install to Generic x86](https://github.com/CPFL/Autoware/wiki/Generic-x86-Docker)

## NVIDIA DRIVE

We provide Docker environments for the NVIDIA DRIVE platform with support from NVIDIA Corporation. To access any of the following environments, you should have signed their NDA/SLA to access NVIDIA DevZone and, in some case, should have been authorized to access internal details of NVIDIA DriveWorks SDK.

#### DRIVE PX2

If you are using the DRIVE PX2 platform, you can choose Docker with or without NVIDIA DriveWorks. With NVIDIA DriveWorks, you may leverage NVIDIA self-driving capabilities, such as line detection and object detection using DriveNet. Without DriveWorks, on the other hand, all self-driving capabilities are covered by Autoware, thus for example object detection is based on SSD or YOLO2. For more details, try it our yourself.

[>> Install to DRIVE PX2](https://github.com/CPFL/Autoware/wiki/DRIVE-PX2-Docker)

#### DRIVE Xavier

Coming soon.

## 96Boards

#### SynQuencer E

The preferred main memory size is 16GB to 32GB.

[>> Install to SynQuencer E](https://github.com/CPFL/Autoware/wiki/SynQuencer-E-Docker)