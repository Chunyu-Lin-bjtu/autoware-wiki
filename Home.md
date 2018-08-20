![Autoware.AI](https://www.autoware.ai/static/img/autoware_web_img.png)

## Welcome to the Autoware Wiki

Autoware is _ROS-based open-source software_, enabling self-driving mobility to be deployed in open city areas. It provides, but not limited to, the following modules. 

_Localization_ is achieved by **3D maps** and **SLAM** algorithms in combination with **GNSS** and **IMU** sensors. 
_Detection_ uses **cameras** and **LiDARs** with **sensor fusion** algorithms and **deep neural networks**. 
_Prediction_ and _Planning_ are based on **probabilistic robotics** and **rule-based systems**, partly using **deep neural networks** as well. 
The output of Autoware to the vehicle is a twist of **velocity** and **angular velocity** (also **curvature**). This is a part of _Control_, though the major part of _Control_ is supposed to reside in the **by-wire** controller of the vehicle, where **PID** and **MPC** algorithms are often adopted. 

All in all, Autoware provides a complete software stack for self-driving technology. Join Autoware now, and your contribution will be loved by the world.

## Getting started

You can easily install Autoware using Docker and run the demo using ROSBAG.

1. [Installation](https://github.com/CPFL/Autoware/wiki/Installation)
1. [Demo](https://github.com/CPFL/Autoware/wiki/Demo)

## How to contribute

* Coding

Autoware is managed by Github at [https://github.com/cpfl/Autoware](https://github.com/cpfl/Autoware). You are always welcome to fork it and send your contribution as a pull request to the repository. Whenever you contribute to coding of Autoware modules, however, please respect and follow the [Contribution Rules](https://github.com/CPFL/Autoware/wiki/Contribution-Rules) so that the repository can keep organized. To install Autoware, we strongly recommend you using [Autoware Docker](https://github.com/CPFL/Autoware/wiki/Docker). Otherwise, you can follow the instruction provided by [README.md](https://github.com/CPFL/Autoware/blob/master/README.md).

* Field testing

Autoware is widely used in research and development on self-driving technology. Many Autoware-based self-driving cars have shown amazing demonstrations of on public roads. A remarkable story in early days is that Udacity has adopted Autoware (see the [story](https://asia.nikkei.com/Business/Companies/Udacity-Tier-IV-tie-up-in-driverless-car-development)) for their [Self-Driving Car Nanodegree Program](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013), and one spinout team has made a successful field demonstration on El Camino Real, CA (see the [story](http://www.businessinsider.com/voyage-autonomous-taxi-udacity-2017-4)). Other examples include: [[Palo Alto, USA](https://www.youtube.com/watch?v=EUqOzfgc4UY&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=7)][[Aichi, Japan](https://www.youtube.com/watch?v=npQMzH3j_d8&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=4)][[Tokyo, Japan](https://www.youtube.com/watch?v=FjjkA96MuD8&index=6&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU)]. It is impressive that a few Japanese teams have made Autoware-based driverless cars on public roads: [[Aichi, Japan](https://www.youtube.com/watch?v=aDt__zW53Qs&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=2)][[Shimane, Japan](https://www.youtube.com/watch?v=RimuPT6e-Oo&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=9)][[Tokushima, Japan](https://www.youtube.com/watch?v=rQwIC2wZlzQ&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=11)]. The first media coverage of Autoware-based driverless car is [here](https://www.youtube.com/watch?v=_IX1uUjrF7M). We appreciate many successors of field testing. Please also upload your ROSBAG files recorded during field testing to [ROSBAG STORE](https://rosbag.tier4.jp) so that other Autoware and ROS users who do not own cars can reproduce the scenes and simulate the functions.

* Production

Autoware can also be used for products and services. The following are some examples. [Tier IV](https://www.tier4.jp) offers a compact self-driving development kit, called [AI Pilot](https://tier4.jp/en/mobility/aipilot.php), where cameras, LiDAR, GPS/IMU, and computers (DRIVE PX2, R-Cars, etc.) are all integrated in a package. [AutonomouStuff](https://autonomoustuff.com/) distributes [by-wire vehicles](https://autonomoustuff.com/product/astuff-automotive/), where Autoware is available. [ZMP](https://www.zmp.co.jp) also distributes Autoware-preinstalled vehicles. [Aisan Technology](http://www.aisantec.co.jp/english/) provides high-definition/accuracy/resolution 3D maps that use the mapping format supported by Autoware (see [videos](https://www.youtube.com/channel/UClndQXbGrlo_cWR7tzu5LOQ)). We appreciate these companies choosing Autoware as a commercial solution, and hope to see more and more companies adopting Autoware in production.