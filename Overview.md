![Autoware Overview](https://github.com/CPFL/Autoware/blob/master/docs/images/autoware_overview.png)

## Sensing

Autoware supports Camera, LiDAR, IMU, and GPS as primary sensors. The following are examples of those that have been already verified with Autoware through the field testing. Technically speaking, if not verified, almost all types of Camera, LiDAR, IMU, and GPS should be available for Autoware, as far as sensor driver software is provided.

### Camera

* PointGrey (FLIR) Grasshopper 3 (USB/GigE) [[link](https://www.ptgrey.com/grasshopper3-usb3-vision-cameras)]
* PointGrey (FLIR) Flea 2/3 (USB/GigE) [[link](https://www.ptgrey.com/flea3-gige-vision-cameras)]
* PointGrey (FLIR) Blackfly (USB3/GigE) [[link](https://www.ptgrey.com/blackfly-usb3-vision-cameras)]
* Baumer VLG-22C (USB3/GigE) [[link](https://www.baumer.com/sg/en/product-overview/image-processing-identification/industrial-cameras/long-term-availability/visiline-series/ams-cmosis-sensors/vlg-22c/p/24060)]
* Baumer VCXU-24C (USB3/GigE) [[link](https://www.baumer.com/us/en/product-overview/image-processing-identification/industrial-cameras/cx-series/usb-3-0-interface/vcxu-24c/p/23796)]
* Generic UVC Webcam (USB2/3)

_You may use multiple units of the above camera sensors together but they should be configured separately for individual purposes, such as object detection and traffic light recognition, as Autoware does not support concatenating multiple images into a single large image._

### LiDAR

* VELODYNE HDL-64E (S1/S2/S3) [[link](http://velodynelidar.com/hdl-64e.html)]
* VELODYNE HDL-32E [[link](http://velodynelidar.com/hdl-32e.html)]
* VELODYNE VLP-16 [[link](http://velodynelidar.com/vlp-16.html)]
* VELODYNE VLP-16 Lite [[link](http://velodynelidar.com/vlp-16-lite.html)]
* VELODYNE VLP-16 Hi-Res [[link](http://velodynelidar.com/vlp-16-hi-res.html)]
* HOKUYO YVT-35LX (3D-URG) [[link](https://www.hokuyo-aut.co.jp/search/single.php?serial=165)]
* HOKUYO UTM-30LX (TOP-URG) [[link](http://www.senteksolutions.com/products/scanning-laser-rangefinders/utm-30lx)]
* SICK LMS511 [[link](https://www.sick.com/us/en/detection-and-ranging-solutions/2d-lidar-sensors/lms5xx/lms511-10100-pro/p/p215941)]
* PIONEER 3D LiDAR (yet to be released) [[link](http://global.pioneer/en/news/press/2017/pdf/1130-1.pdf)]

_You may combine multiple units of the above LiDAR sensors through TF, providing rich fused pointcloud data for more precise object detection, tracking, and localization._

### RADAR

* Delphi ESR [[link](https://autonomoustuff.com/product/delphi-esr-2-5-24v/)]

_Autoware sensing is mainly based on LiDAR scanners but milliwave RADAR is also available for the purpose of long-distance object tracking._

### IMU

* Memsic VG440 [[link](http://www.aceinna.com//VG440CA-200|400)]
* Xsens MTi-300 [[link](https://www.xsens.com/products/mti-100-series/)]
* MicroStrain 3DM-GX5-15 [[link](http://www.microstrain.com/inertial/3dm-gx5-15)]
* Novatel IGM S1 IMU [[link](https://www.novatel.com/products/span-gnss-inertial-systems/span-imus/span-mems-imus/imu-igm-s1/)]

_Currently, advanced users of Autoware are not very in favor of IMU, because SLAM-based localization augmented by 3D maps and odometers is pretty reliable without IMU. However, we believe IMU is still useful in some scenario and Autoware supports an interface to add IMU data to localization modules._

### GPS/GNSS

* Javad DELTA-3 [[link](https://www.javad.com/jgnss/products/receivers/delta-3.html)]
* MITSUBISHI AQLOC (only available in Japan) [[link](http://www.mitsubishielectric.co.jp/news/2017/1129.html)]
* Trimble NetR9 [[link](http://www.trimble.com/Infrastructure/Trimble-NetR9.aspx)]
* Leica Viva GS25 [[link](https://leica-geosystems.com/products/gnss-systems/receivers/leica-viva-gs10-gs25)]
* Applanix APX-15 UAV [[link](https://www.applanix.com/products/dg-uavs.htm)]

_GPS/GNSS receivers typically generate NMEA-compliant sentence (text), which is entirely supported by Autoware, via the serial interface. Therefore, we believe that virtually all GPS/GNSS products would be available for Autoware with the existing nmea2tfpose node._