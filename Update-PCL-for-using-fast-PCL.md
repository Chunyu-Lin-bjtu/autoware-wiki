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