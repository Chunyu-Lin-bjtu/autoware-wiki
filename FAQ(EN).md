#Where is install script?
https://github.com/NavIV/automation-scripts

#How to update PCL?
Update PCL for using fast PCL
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

#Why does Autoware need root privileges?
Autoware changes the nice value and also changes the process scheduling policy.
https://github.com/CPFL/Autoware/blob/master/ros/src/util/packages/runtime_manager/scripts/proc_manager.py#L102-L119
In addition, root may be necessary for the execution of the USB-UVC driver.