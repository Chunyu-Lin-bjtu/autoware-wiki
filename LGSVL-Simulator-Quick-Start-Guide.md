# Required equipments

![screenshot from 2019-01-17 15-10-55](https://user-images.githubusercontent.com/10348912/51299434-d4787e00-1a6b-11e9-9f74-ccc166e2ec83.png)

# Setup Required Software
## In Simulator Windows Machine
### Install Unity
Install Unity 2018.2.4. Windows link: https://unity3d.com/get-unity/download/archive
### Invert LGSVL Simulator Steering Angle (I think this process removed in the future.)
In Assets/Scripts/VehicleInputController.cs

![image](https://user-images.githubusercontent.com/10348912/51301272-f4ab3b80-1a71-11e9-869c-02edbc86c342.png)

### Setup LGSVL Simulator Launcher
```
git clone https://github.com/tier4/lgsvl_simulator_launcher.git
cd lgsvl_simulator_launcher
pip install pipenv
pipenv shell
python app.py
```

### Compile simulator with batch mode
See : https://github.com/lgsvl/simulator/issues/55

## In Autoware linux Machine
### Setup Autoware.
https://github.com/CPFL/Autoware/wiki/Installation

### download pointcloud map and other datas
### install git lfs
```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt update
sudo apt install git-lfs
```

### download data from lgsvl repo
```
git clone git@github.com:lgsvl/autoware-data.git
```

## Making waypoints with Autoware

### load pointcloud data  
![pointcloud map](https://camo.qiitausercontent.com/435d9952ed982aa1fd74f4de9b399f8dd7ed5f22/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3136303334362f36643935313234612d613866342d363166632d393631362d6530363833376433353033392e706e67)  

load pointcloud data under this directory.  
```
autoware-data/data/map/pointcloud_map_sf_portion/
```

### setup in sensing tab
enabele voxel_grid_filter

### setup in computing tab
enable ndt_matching,vel_pose_connect

### launch LGSVL simulator and bridge.
open simulation tab and click LGSVL simulator button.
Input simulator Machin IP address and LGSVL Simulator Launcher Port.
![screenshot from 2019-01-17 16-21-57](https://user-images.githubusercontent.com/10348912/51304525-c599c780-1a7b-11e9-88c9-0f975d9bacc5.png)

write config .json file like below and load the .json file from the UI.

```
{
  "bin_type" : "tier4-develop",
  "initial_configuration" : {
    "map" : "SanFrancisco",
    "time_of_day" : 12.0,
    "freeze_time_of_day" : true,
    "fog_intensity" : 0.0,
    "rain_intensity" : 0.0,
    "road_wetness" : 0.0,
    "enable_traffic" : true,
    "enable_pedestrian" : true,
    "traffic_density" : 300
  },
  "vehicles" : 
  [
    {
      "type" : "XE_Rigged-autoware",
      "address" : "$(autoware_machine_ip)",
      "port" : 9090,
      "command_type" : "twist",
      "enable_lidar" : true,
      "enable_gps" : true,
      "enable_main_camera" : true,
      "enable_high_quality_rendering" : true,
      "position" : {"n" : 4140310.4, "e" : 590681.5, "h" : 10},
      "orientation" : {"r" : 0.0, "p" : 0.0, "y" : 269.9}
    }
  ]
}
```

![screenshot from 2019-01-17 16-24-41](https://user-images.githubusercontent.com/10348912/51304799-71431780-1a7c-11e9-93cc-c9a3f652290d.png)

### Making waypoints with simulator.
enable waypoint_saver in runtime_manager
Drive simulated cars by using G29 Steering Wheel Controller.

## Autonomous Driving with Autoware.
enable ndt_matching,vel_pose_connect,lane_rule,lane_sotp,lane_select,obstacle_void,velocity_set,pure_pursuit,twist_filter,waypoint_loader in runtime_manager.

### demonstration
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/cBmIiR3jRvE/0.jpg)](https://www.youtube.com/watch?v=cBmIiR3jRvE&feature=youtu.be)