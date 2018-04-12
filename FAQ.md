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
Computation cost becomes smaller if you use larger voxel grid size. We use 2.0 meter by default because it keeps accuracy of localization and computation finishes in the measurement interval of the scan.	

### Can you explain the concept of resolution in ndt mapping or matching?
If you want to know the concept of NDT, please refer to the following paper.
http://onlinelibrary.wiley.com/doi/10.1002/rob.20204/abstract

### What is the difference between ndt_mapping and lazy ndt_mapping?
lazy_ndt_mapping does not use all points for matching while ndt_mapping uses all the points as reference. lazy_ndt_mapping uses only three previous scans as reference by default. lazy_ndt_mapping is faster than ndt_mapping, but with lower accuracy.

### I just want to use ndt_mapping or icp_mapping with my own data only, instead of running Autoware everytime, but everytime I try to run ndt_mapping isolated, I get an error.

ndt_localizer package depends on runtime_manager package in relation to message generation. Therefore you need to build the all packages in Autoare using ./catkin_make_release in Autoware/ros directory.

### Can I use my '.pcap' file to run autoware mapping and then save the result?
Yes. First, convert pcap to rosbag.
http://answers.ros.org/question/213080/convert-raw-velodyne-vlp16-pcap-to-bagfile/
The rosbag includes the topic, velodyne_packets, so you have to convert the topic from /velodyne_packets to /points_raw using VLP-16 driver in Sensing tab.

### My map size is huge. Can I reduce the map size?
Yes. You can reduce the file size using voxel grid filter. It is in the Map tab.

### My map size is over 1GB. I get an error saying "a message of over a gigabyte was predicted in tcpros. that seems highly unlikely, so I'll assume protocol synchronization is lost". What should I do?
Due to ROS specification, if messages over 1GB is published, the error you mentioned occurs. ndt_mapping node publishes all the point cloud previously built, so if the map becomes larger up to a certain size, the message can not be published. If you want to create wide area map, you can use approximate_ndt_mapping instead of ndt_mapping. The node loads and publishes a part of the map, so the error above does not occur.

