![Autoware Version 2.x Overview](https://github.com/CPFL/Autoware/blob/master/docs/images/autoware_overview.png)

## Sensing

Autoware supports Camera, LiDAR, IMU, and GPS as primary sensors. The following are examples of those already verified with Autoware through field testing. Technically speaking, if not verified, almost all types of Camera, LiDAR, IMU, and GPS should be available for Autoware, as far as sensor driver software is provided.

### Camera

* PointGrey (FLIR) Grasshopper 3 (USB/GigE) [[link](https://www.ptgrey.com/grasshopper3-usb3-vision-cameras)]
* PointGrey (FLIR) Flea 2/3 (USB/GigE) [[link](https://www.ptgrey.com/flea3-gige-vision-cameras)]
* PointGrey (FLIR) Blackfly (USB3/GigE) [[link](https://www.ptgrey.com/blackfly-usb3-vision-cameras)]
* Baumer VLG-22C (USB3/GigE) [[link](https://www.baumer.com/sg/en/product-overview/image-processing-identification/industrial-cameras/long-term-availability/visiline-series/ams-cmosis-sensors/vlg-22c/p/24060)]
* Baumer VCXU-24C (USB3/GigE) [[link](https://www.baumer.com/us/en/product-overview/image-processing-identification/industrial-cameras/cx-series/usb-3-0-interface/vcxu-24c/p/23796)]
* Allied Vision Camera Mako G-319C (PoE GigE) [[link](https://www.alliedvision.com/en/products/cameras/detail/Mako%20G/G-319.html)]
* Generic UVC Webcam (USB2/3)

_Multiple Camera sensors are supported, however they should be configured separately for individual purposes. Please verify the documentation on ROS on using namespaces or name for each instance. Autoware separates each camera for a purpose such as object detection and traffic light recognition. Inherently, Autoware does not support concatenating multiple images into a single large image._

### LiDAR

* VELODYNE HDL-64E (S1/S2/S3) [[link](http://velodynelidar.com/hdl-64e.html)]
* VELODYNE HDL-32E [[link](http://velodynelidar.com/hdl-32e.html)]
* VELODYNE VLP-32C [[link](http://velodynelidar.com/vlp-32c.html)]
* VELODYNE VLP-16 [[link](http://velodynelidar.com/vlp-16.html)]
* VELODYNE VLP-16 Lite [[link](http://velodynelidar.com/vlp-16-lite.html)]
* VELODYNE VLP-16 Hi-Res [[link](http://velodynelidar.com/vlp-16-hi-res.html)]
* HOKUYO YVT-35LX (3D-URG) [[link](https://www.hokuyo-aut.co.jp/search/single.php?serial=165)]
* HOKUYO UTM-30LX (TOP-URG) [[link](http://www.senteksolutions.com/products/scanning-laser-rangefinders/utm-30lx)]
* SICK LMS511 [[link](https://www.sick.com/us/en/detection-and-ranging-solutions/2d-lidar-sensors/lms5xx/lms511-10100-pro/p/p215941)]
* PIONEER 3D LiDAR (yet to be released) [[link](http://global.pioneer/en/news/press/2017/pdf/1130-1.pdf)]

_You may combine multiple units of the above LiDAR scanners through TF, providing rich fused pointcloud data for more precise object detection, tracking, and localization. Please check Velodyne's documentation on how to use multiple sensors in the same network._

### RADAR

* Delphi ESR [[link](https://autonomoustuff.com/product/delphi-esr-2-5-24v/)]

_Autoware sensing is mainly based on LiDAR scanners. Milliwave RADAR drivers are also available for the purpose of long-distance object tracking. However, its integration to the perception package is still a work in progress._

### IMU

* Memsic VG440 [[link](http://www.aceinna.com//VG440CA-200|400)]
* Xsens MTi-300 [[link](https://www.xsens.com/products/mti-100-series/)]
* MicroStrain 3DM-GX5-15 [[link](http://www.microstrain.com/inertial/3dm-gx5-15)]
* Novatel IGM S1 IMU [[link](https://www.novatel.com/products/span-gnss-inertial-systems/span-imus/span-mems-imus/imu-igm-s1/)]

_Currently, advanced users of Autoware are not in favor of IMU, because SLAM-based localization augmented by 3D maps and odometers is reliable enough without the use of an IMU. However, we believe IMU is still useful in some scenarios, therefore Autoware supports IMU drivers and data integration into the localization modules._

### GPS/GNSS

* Javad DELTA-3 [[link](https://www.javad.com/jgnss/products/receivers/delta-3.html)]
* MITSUBISHI AQLOC (only available in Japan) [[link](http://www.mitsubishielectric.co.jp/news/2017/1129.html)]
* Trimble NetR9 [[link](http://www.trimble.com/Infrastructure/Trimble-NetR9.aspx)]
* Leica Viva GS25 [[link](https://leica-geosystems.com/products/gnss-systems/receivers/leica-viva-gs10-gs25)]
* Applanix APX-15 UAV [[link](https://www.applanix.com/products/dg-uavs.htm)]

_GPS/GNSS receivers typically generate NMEA-compliant sentences (text strings), which is entirely supported by Autoware, via the serial interface. Therefore, we believe that as long as the device is NMEA compliant, virtually all GPS/GNSS products, would be compatible for Autoware with the existing nmea2tfpose node._

## Computing/Perception

The perception capability of Autoware is composed of Localization, Detection, and Prediction. Localization is achieved by 3D maps and SLAM algorithms in combination with GNSS and IMU sensors. Detection uses cameras and LiDARs with sensor fusion algorithms and deep neural networks. Prediction is based on the results of Localization and Detection. The following are the highlighted packages and functions provided by Autoware.

### Localization

* **lidar_localizer** computes the (_x, y, z, roll, pitch, yaw_) position of the ego vehicle in the global coordinate, using the scanned data from LiDAR and the pre-installed 3D map information. We recommend the Normal Distributions Transform (NDT) algorithm for the LiDAR scan matching with the 3D map, while the Iterative Closet Point (ICP) algorithm is also supported.  
* **gnss_localizer** transforms the NMEA message from a GNSS receiver to the (_x, y, z, roll, pitch, yaw_) position. This result can be used as the position of the ego vehicle alone, while it can also be used to initialize and complement the result of **lidar_localizer**.
* **dead_reckoner** mainly uses an IMU sensor to predict the next-frame position of the ego-vehicle and also interpolate the result of **lidar_localizer** and **gnss_localizer**. 

### Detection

* **lidar_detector** provides LiDAR-based object detection capabilities. The basic performance comes from the Euclidean Clustering algorithm, which finds clusters of the LiDAR scan (point cloud) above the ground. To classify the clusters, DNN-based algorithms are also supported, such as VoxelNet and LMNet.
* **lidar_tracker** identifies moving objects detected by **lidar_detector** on a time basis. The result of tracking can be used for prediction of the object behavior and estimation of the object velocity. The tracking algorithm is based on the Kalman Filters. Another variant supports the Particle Filters as well. 
* **vision_detector** provides vision-based object detection capabilities. The main algorithms include SSD and Yolo (v2 & v3), which are both designed to perform single DNNs for real-time performance. Multiple classes of detection are supported, such as cars and passengers.
* **vision_tracker** is currently not actively used but it implements the Kalman Filters to predict the next-frame position of moving objects detected by **vision_detector**.
* **fusion_detector** uses both point cloud data from LiDAR scanners and image data from cameras to achieve more accurate object detection on the 3D coordinate. The positions of LiDAR scanner(s) and camera(s) must be calibrated in advance. The current implementation is based on the MV3D algorithm with a minor extension of the network as compared to the original algorithm.
* **fusion_tracker** uses either the result of **fusion_detector** alone or the fused result of **lidar_detector** and **vision_detector**. In either case, the moving objects are identified on a time and continuously tracked for prediction of the object behavior and estimation of the object velocity. This package should outperform **lidar_tracker**, though it is still a work in progress.

### Prediction

* **moving_predictor** uses the result of object tracking described above to predict the future trajectories of neighbor moving objects, such as cars and passengers.
* **collision_predictor** uses the result of **moving_predictor** to predict if the ego vehicle is involved in possible collision against the moving objects. The waypoint trajectory and the velocity information of the ego vehicle is also required as input data in addition to the result of object tracking.
* **cutin_predictor** uses the same pieces of information as **collision_predictor** to predict if neighbor cars cut in the front of the ego vehicle.  

## Computing/Decision

The decision module of Autoware bridges across the perception and the planning modules. Upon the result of perception, Autoware decides a driving behavior, represented by a finite state machine, so that an appropriate planning function can be selected. The current approach to decision making is a rule-based system.

### Intelligence

* **decision_maker** subscribes a large set of topics related to the result of perception, map information, and the current state in order to publish the next-moment state topic. This state change will activate an appropriate planning function.

### State

* **state_machine** changes the state within pre-defined rules, orchestrating with **decision_maker**.

## Computing/Planning

The last piece of computing in Autoware is a planning module. The role of this module is to make plans of global mission and local (temporal) motion based on the results of the perception and the decision modules. A global mission is often determined when the ego vehicle starts or restarts, while a local motion is updated according to state changes. For example, the velocity of the ego vehicle is planned to become zero in front of an object with a safety margin or at a stop line if the state of Autoware is set to "stop". Another example is that the trajectory of the ego vehicle is planned to bypass an obstacle if the state of Autoware is set to "avoid". The primary packages included in the planning module are the following.

### Mission

* **route_planner** searches for a global route to the destination. The route is represented by a set of intersections in the road network.
* **lane_planner** determines which lanes to be used along with the route published by **route_planner**. The lanes are represented by an array of waypoints, i.e., multiple waypoints, each of which corresponds to a single lane, are published by this package.
* **waypoint_planner** can be alternatively used to generate a set of waypoints to the destination. This package differs from **lane_planner** in that it publishes a single stroke of waypoints rather than an array of waypoints. 
* **waypoint_maker** is a utility tool to save and load hand-made waypoints. To save waypoints to the specified file, you drive a vehicle manually while localization is activated, and Autoware records waypoints of the driving path with velocity information. The recorded waypoints can be loaded later on from the specified file to have the motion planning module subscribe them to follow that path.

### Motion
* **velocity_planner** updates a velocity plan on the waypoints subscribed from either **lane_planner**,  **waypoints_planner**, or *waypoints_maker** so as to speed down/up against surrounding vehicles and road features such as stop lines and traffic lights. Note that the velocity information embedded in the given waypoints is static, while this package updates a velocity plan according to driving scenes. 
* **astar_planner** implements the Hybrid-State A* search algorithm that generates a feasible trajectory from the current position to the specified position. This package can be used for obstacle avoidance and sharp turns on the given waypoints as well as routing in free space such as parking lots.
* **adas_lattice_planner** implements the State Lattice planning algorithm that generates multiple feasible trajectories ahead of the current position based on spline curves, a pre-defined parameter table, and the ADAS Map (a.k.a., Vector Map) information. This package can be used mostly for obstacle avoidance and lane changes.
* **waypoint_follower** implements the Pure Pursuit algorithm that generates a twisted set of velocity and angular velocity (or just angle) to move the ego vehicle by uniform circular motion to a target waypoint over the given waypoints. This package should be used in combination with **velocity_planner**, **astar_planner**, and/or **adas_lattice_planner**. The published twisted set of velocity and angular velocity (or just angle) will be read by a vehicle controller or a by-wire interface, and finally the ego vehicle is controlled autonomously.