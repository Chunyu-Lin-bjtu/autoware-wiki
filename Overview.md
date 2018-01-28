![Autoware Overview](https://github.com/CPFL/Autoware/blob/master/docs/images/autoware_overview.png)

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

* PointGrey (FLIR) Grasshopper 3 (USB/GigE) [[link](https://www.ptgrey.com/grasshopper3-usb3-vision-cameras)]
* PointGrey (FLIR) Flea 2/3 (USB/GigE) [[link](https://www.ptgrey.com/flea3-gige-vision-cameras)]
* PointGrey (FLIR) Blackfly (USB3/GigE) [[link](https://www.ptgrey.com/blackfly-usb3-vision-cameras)]
* Baumer VLG-22C (USB3/GigE) [[link](https://www.baumer.com/sg/en/product-overview/image-processing-identification/industrial-cameras/long-term-availability/visiline-series/ams-cmosis-sensors/vlg-22c/p/24060)]
* Baumer VCXU-24C (USB3/GigE) [[link](https://www.baumer.com/us/en/product-overview/image-processing-identification/industrial-cameras/cx-series/usb-3-0-interface/vcxu-24c/p/23796)]
* Generic UVC Webcam (USB2/3)

_You may use multiple units of the above camera sensors together but they should be configured separately for individual purposes, such as object detection and traffic light recognition, as Autoware does not support concatenating multiple images into a single large image._
