## What Is Autoware

Autoware is ROS-based open-source software, enabling self-driving mobility to perform in open city areas. It provides, but not limited to, the following modules. _Localization_ is achieved by **3D maps** and **SLAM** algorithms in combination with **GNSS** and **IMU** sensors. _Detection_ uses **cameras** and **LiDARs** with **sensor fusion** algorithms and **deep neural networks**. _Prediction_ and _Planning_ are based on **probabilistic robotics** and **rule-based systems**, partly using **deep neural networks** as well. The output of Autoware to the vehicle is a twist of **velocity** and **angular velocity** (also **curvature**). This is a part of _Control_, though the major part of _Control_ is supposed to reside in the **by-ware** controller of the vehicle, where **PID** and **MPC** algorithms are often adopted. All in all, Autoware provides a complete software stack for self-driving technology. Join Autoware now, and your contribution will be there.

## How To Contribute</h2>

* Coding

Autoware is managed by Github at [https://github.com/cpfl/Autoware](https://github.com/cpfl/Autoware). You are always welcome to fork it and send your contribution as a pull request to the repository. Whenever you contribute to coding of Autoware modules, however, please respect and follow our [branching model](https://github.com/CPFL/Autoware/blob/master/docs/en/branching_model.md) policy so that the repository can keep organized. To install Autoware, we strongly recommend you using our Docker environments: [[Generic x86](https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-Generic-x86)][[DRIVE PX2](https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-DRIVE-PX2)]. Otherwise, you can visit [https://github.com/cpfl/Autoware](https://github.com/cpfl/Autoware), and follow the instructions in [README.md](https://github.com/CPFL/Autoware/blob/master/README.md).

* Field Testing

Autoware is widely used in research and development of self-driving technology. The most highlighted story of Autoware is its high-quality capability for field testing. So far many Autoware-based self-driving cars have shown amazing demonstrations of on public roads. A remarkable example is that Udacity has adopted Autoware (see the [story](https://asia.nikkei.com/Business/Companies/Udacity-Tier-IV-tie-up-in-driverless-car-development)) for their [Self-Driving Car Nanodegree Program](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013), and one spinout team has made a successful field demonstration on El Camino Real, CA (see the [story](http://www.businessinsider.com/voyage-autonomous-taxi-udacity-2017-4)). Other examples include: [[Palo Alto](https://www.youtube.com/watch?v=EUqOzfgc4UY&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=7)][[Ros Gatos](https://www.youtube.com/watch?v=bYpRhh3wGPo&index=8&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU)][[Aichi, Japan](https://www.youtube.com/watch?v=5DaQBZvZwAI&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=6)]. It is also impressive that a few Japanese teams have shown Autoware-based driverless cars, one of the world's first driverless cars on public roads: [[Shimane](https://www.youtube.com/watch?v=RimuPT6e-Oo&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=9)][[Toyama](https://www.youtube.com/watch?v=S1uM65zaVQc&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=10)][[Tokushima](https://www.youtube.com/watch?v=rQwIC2wZlzQ&list=PLMV3EZ9zjNbIkOWvjaY2iU8LVC-pUQMOU&index=11)]. The first media coverage of Autoware-based driverless car is [here](https://www.youtube.com/watch?v=_IX1uUjrF7M). We appreciate many successors of field testing. Please also upload your ROSBAG files recorded during field testing to [ROSBAG STORE](https://rosbag.tier4.jp) so that other Autoware and ROS users who do not own cars can reproduce the scenes and simulate the functions.

* Production

Autoware can also be used for products and services. [Tier IV](http://www.tier4.jp) offers a compact self-driving development kit, called [AI Pilot](http://tier4.jp/en/computers.php), where cameras, LiDAR, GPS/IMU, and computers (DRIVE PX2, R-Cars, etc.) are all integrated in a package. [AutonomouStuff](https://autonomoustuff.com/) distributes [by-wire vehicles](https://autonomoustuff.com/product/astuff-automotive/), where Autoware can be preinstalled as an option. [ZMP](https://www.zmp.co.jp) also distributes Autoware-preinstalled vehicles. [Aisan Technology](http://www.aisantec.co.jp/english/) provides high-definition/accuracy/resolution 3D maps that use the mapping format supported by Autoware (see [videos](https://www.youtube.com/channel/UClndQXbGrlo_cWR7tzu5LOQ)). We appreciate these companies selecting Autoware as a commercial solution, and hope to see more and more companies adopting Autoware in production.

## Autoware Wiki

### Developers Guide

1. [Contribution Rules](https://github.com/CPFL/Autoware/wiki/Contribution-Rules) (**Must Read**)
1. [Overview](https://github.com/CPFL/Autoware/wiki/Overview)
1. [Packages](https://github.com/CPFL/Autoware/wiki/Packages)

### Users Guide (Mandatory)

1. [Installation](https://github.com/CPFL/Autoware/wiki/Installation)
1. [Demo Data](https://github.com/CPFL/Autoware/wiki/Demo-Data)
1. [Sensing](https://github.com/CPFL/Autoware/wiki/Sensing)
1. [Localization](https://github.com/CPFL/Autoware/wiki/Localization)
1. [Detection](https://github.com/CPFL/Autoware/wiki/Detection)
1. [Decision](https://github.com/CPFL/Autoware/wiki/Decision)
1. [Planning](https://github.com/CPFL/Autoware/wiki/Planning)
1. [Control](https://github.com/CPFL/Autoware/wiki/Control)
1. [Actuation](https://github.com/CPFL/Autoware/wiki/Actuation)

### Users Guide (Optional)

1. [Mapping](https://github.com/CPFL/Autoware/wiki/Mapping)
1. [Calibration](https://github.com/CPFL/Autoware/wiki/Calibration)
1. [FAQ](https://github.com/CPFL/Autoware/wiki/FAQ)