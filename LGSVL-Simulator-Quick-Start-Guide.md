# Required equipments

![screenshot from 2019-01-17 15-10-55](https://user-images.githubusercontent.com/10348912/51299434-d4787e00-1a6b-11e9-9f74-ccc166e2ec83.png)

# Setup Required Software.
## In Simulator Windows Machine
1. Install Unity
Install Unity 2018.2.4. Windows link: https://unity3d.com/get-unity/download/archive
1. Invert LGSVL Simulator Steering Angle (I think this process removed in the future.)
In Assets/Scripts/VehicleInputController.cs

![image](https://user-images.githubusercontent.com/10348912/51301272-f4ab3b80-1a71-11e9-869c-02edbc86c342.png)

1. Compile simulator with batch mode.
See : https://github.com/lgsvl/simulator/issues/55

## In Autoware linux Machine.


### download pointcloud map and other datas.
1. install git lfs
```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt update
sudo apt install git-lfs
```

1. download data from lgsvl repo
```
git clone git@github.com:lgsvl/autoware-data.git
```

1. load pointcloud data  
![pointcloud map](https://camo.qiitausercontent.com/435d9952ed982aa1fd74f4de9b399f8dd7ed5f22/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3136303334362f36643935313234612d613866342d363166632d393631362d6530363833376433353033392e706e67)  

load pointcloud data under this directory.  
```
autoware-data/data/map/pointcloud_map_sf_portion/
```

3. setup in sensing tab
enabele voxel_grid_filter

4. setup in computing tab
enable ndt_matching,vel_pose_connect,lane_rule,lane_sotp,lane_select,obstacle_void,velocity_set,pure_pursuit,twist_filter,waypoint_loader

### demonstration
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/npTvZ09ijPA/0.jpg)](https://www.youtube.com/watch?v=npTvZ09ijPA&t=109s)