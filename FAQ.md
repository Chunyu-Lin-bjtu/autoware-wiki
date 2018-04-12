# Setup/Installation
### Where is install script?
https://github.com/NavIV/automation-scripts

### How to update PCL?
You need PCL Ver.1.7.2 to enable the fast PCL library. If the version of PCL is 1.7.1 or under, please update in the following steps.
```
sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl
sudo apt-get update
sudo apt-get dist-upgrade
```
Then, if Autoware is build, you can see the error message.
You should set the LIBRARY_PATH.
```
export LIBRARY_PATH=/usr/lib/OpenNI2/Drivers:$LIBRARY_PATH
```

### Why does Autoware need root privileges?
Autoware changes the nice value and also changes the process scheduling policy.
https://github.com/CPFL/Autoware/blob/master/ros/src/util/packages/runtime_manager/scripts/proc_manager.py#L102-L119
In addition, root may be necessary for the execution of the USB-UVC driver.

# Mapping/Localization

### Why does mapping needed in the slam?
In Autoware, localization(ndt_matching) and mapping(ndt_mapping) are completely separate functions. ndt_mapping is a function that create a map in a unknown environment from scratch so you don't need a map. On the other hand, ndt_matching is a localization function within a map so map is needed as a input of the function.

The reason why we need to match the scan and the existing map is, it is faster and more accurate than matching the current scan and the previous scans. Simultaneously localize and mapping using NDT can not be done in real-time so far. If you want to know about NDT algorithm, please refer to the following paper.

### What is the relationship between the grid size of voxel grid filter and accuracy of localization?
Theoretically, larger grid sizes decrease the accuracy of localization.

### What criteria should be used to determine voxel grid size?
Computation cost becomes smaller if you use larger voxel grid size. We use 2.0 meter by default because it keeps accuracy of localization and computation finishes in the measurement interval of scan.	
