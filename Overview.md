## Supported Sensors

Autoware supports LiDAR, Camera, IMU, and GPS as primary sensors. The following are examples of those that have been already verified through the field testing. Technically speaking, if not verified, almost all types of LiDAR, Camera, IMU, and GPS would be available in Autoware.

### LiDAR

* VELODYNE HDL-64E (S1/S2/S3) [[link](http://velodynelidar.com/hdl-64e.html)]
* VELODYNE HDL-32E [[link](http://velodynelidar.com/hdl-32e.html)]
* VELODYNE VLP-16 [[link](http://velodynelidar.com/vlp-16.html)]
* VELODYNE VLP-16 Lite [[link](http://velodynelidar.com/vlp-16-lite.html)]
* VELODYNE VLP-16 Hi-Res [[link](http://velodynelidar.com/vlp-16-hi-res.html)]
* HOKUYO YVT-35LX (3D-URG) [[link](https://www.hokuyo-aut.co.jp/search/single.php?serial=165)]
* HOKUYO UTM-30LX (TOP-URG) [[link](http://www.senteksolutions.com/products/scanning-laser-rangefinders/utm-30lx)]
* SICK LMS511 [[link](https://www.sick.com/us/en/detection-and-ranging-solutions/2d-lidar-sensors/lms5xx/lms511-10100-pro/p/p215941)]

_You may combine multiple units of the above LiDAR sensors through TF, providing rich fused pointcloud data for more precise object detection, tracking, and localization._

### Camera

* PointGrey (FLIR) Grasshopper 3 (USB/GigE)
* PointGrey (FLIR) Flea 2/3 (USB/GigE)
* PointGrey (FLIR) Blackfly 2 (USB3/GigE)
* Baumer VLG-22 (USB3/GigE)
* Baumer VCXU-24 (USB3/GigE)
* Generic UVC Webcam (USB2/3)