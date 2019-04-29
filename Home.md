![Autoware.AI](https://static.wixstatic.com/media/984e93_bd79992caecb41dab100c391e648d9b8~mv2.png/v1/fill/w_1934,h_1148,al_c/984e93_bd79992caecb41dab100c391e648d9b8~mv2.png)

## Welcome to the Autoware Wiki

Autoware is ROS-based open-source software enabling self-driving vehicles to be deployed in private areas, urban roads, and highways. It provides, but not limited to, the following functional modules. 

_Localization_ is based on **3D high-definition map** data and the **NDT** algorithm. The result of _Localization_ can be complemented by the **Kalman Filter** algorithm using odometry information such as **CAN** messages and **GNSS/IMU** sensors.
 
_Detection_ is empowered by **camera** and **LiDAR** devices in combination with **3D high-definition map** data. The _Detection_ module uses **deep learning** and **sensor fusion** approaches.

_Tracking_ and _Prediction_ are realized with the **Kalman Filter** algorithm, leveraging lane network information provided by **3D high-definition map** data.
 
_Planning_ is based on **probabilistic robotics** and **rule-based systems**, partly using **deep learning** approaches as well. 

_Control_ defines motion of the vehicle with a twist of **velocity** and **angular velocity** (also **curvature**). The _Control_ module falls into both the Autoware stack (**MPC** and **Pure Pursuit**) and the vehicle by-wire controller stack (**PID** variants). 

All in all, Autoware provides a complete software stack for self-driving technology. Join Autoware now, and your contribution will be loved by the world.

## Getting started

You can easily install Autoware using Docker and run the demo using ROSBAG.

1. [Installation](https://github.com/CPFL/Autoware/wiki/Installation)
1. [Demo](https://github.com/CPFL/Autoware/wiki/Demo)