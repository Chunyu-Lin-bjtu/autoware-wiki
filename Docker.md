To install Autoware, we strongly recommend you using our Docker environments: [[Generic x86](https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-Generic-x86)][[DRIVE PX2](https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-DRIVE-PX2)]. The supported version of Autoware is  newer than 1.6.0. In case that you do not want to use Docker for installation, please follow the instruction provided by [README.md](https://github.com/CPFL/Autoware/blob/master/README.md).

## Generic x86 (64 bits)

The supported, but not limited to, computing environments are as follows:

* Intel Core i7 (preferred), Core i5, Atom
* 16GB to 32GB of main memory
* More than 30GB of SSD
* NVIDIA GTX GeForce GPU (980M or higher performance)

[Get Generic x86 Docker](https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-Generic-x86)

## NVIDIA DRIVE

We provide Docker environments for the NVIDIA DRIVE platform with support from NVIDIA Corporation. To access any of the following environments, you should have signed their NDA/SLA to access NVIDIA DevZone and, in some case, have been authorized to access more details of NVIDIA DriveWorks SDK.

### DRIVE PX2

If you are using the DRIVE PX2 platform, you can choose Docker with or without NVIDIA DriveWorks. With NVIDIA DriveWorks, you may leverage NVIDIA self-driving capabilities, such as line detection and object detection using DriveNet. Without DriveWorks, on the other hand, all self-driving capabilities are covered by Autoware, thus for example object detection is based on SSD or YOLO2. For more details, try it our yourself.

[Get DRIVE PX2 Docker](https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-DRIVE-PX2)