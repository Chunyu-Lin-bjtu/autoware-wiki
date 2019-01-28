# Required equipment

![Required equipment](https://user-images.githubusercontent.com/10348912/51299434-d4787e00-1a6b-11e9-9f74-ccc166e2ec83.png)

# Software setup

## Windows simulator machine

### Install Unity

Unity **2018.2.4** is required. Download the Windows installer for this version from the [Unity download archive](https://unity3d.com/get-unity/download/archive) and execute it. Follow the instructions in the installer to install Unity.

### Correct simulator steering angle

The LGSVL simulator steering angle needs to be inverted. In the file `Assets/Scripts/VehicleInputController.cs`, make the following change:

![LGSVL steering angle inversion](https://user-images.githubusercontent.com/10348912/51301272-f4ab3b80-1a71-11e9-869c-02edbc86c342.png)

(This step will become unnecessary in a future update.)

### Setup LGSVL Simulator Launcher

In a terminal, run the following commands to download and set up the LGSVL simulator launcher.

```
git clone https://github.com/tier4/lgsvl_simulator_launcher.git
cd lgsvl_simulator_launcher
pip install pipenv
pipenv shell
python app.py
touch setting.json
```

Open `setting.json` in an editor and paste in the following content.
```
{
[
  {name:stable, path:"C:\Documents\Simulator"},
  {name:develop, path:"C:\Documents\Simulator"}
]
}
```

### Compile simulator with batch mode

LGSVL **cannot** be built using the default Unity Editor build command. As described in [this LGSVL issue](https://github.com/lgsvl/simulator/issues/55), the simulator must be built using batch mode to correctly package assets.

Following the [LGSVL build instructions](https://github.com/lgsvl/simulator/blob/master/Docs/build-instructions.md), build on the command line, ensuring that the `-batchmode` option is specified and the `-buildTarget` is `Windows64`.

## Linux Autoware machine

### Setup Autoware

Follow the [Autoware installation instructions](https://github.com/CPFL/Autoware/wiki/Installation) to install Autoware.

### Download data

Autoware requires a pointcloud map and other data to run. This data can be downloaded from the LGSVL Git large file store.

1. Install Git LFS by running the following commands.

   ```
   curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
   sudo apt update
   sudo apt install git-lfs
   ```

1. Download the data from the LGSVL repository

   ```
   git clone git@github.com:lgsvl/autoware-data.git
   ```

# Waypoint creation with Autoware

## Prepare Autoware

To make waypoints in Autoware, load a pointcloud into Autoware and then drive around in the simulator, saving the waypoints as they are created.

First, Load the pointcloud data into Autoware using the Runtime Manager.

![Map settings tab](https://camo.qiitausercontent.com/435d9952ed982aa1fd74f4de9b399f8dd7ed5f22/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3136303334362f36643935313234612d613866342d363166632d393631362d6530363833376433353033392e706e67)

The pointcloud data can be found in the `autoware-data/data/map/pointcloud_map_sf_portion/` directory.

Several settings need to be set in Autoware:

- `Sensing` tab: Enable `voxel_grid_filter`

- `Computing` tab: Enable `ndt_matching` and `vel_pose_connect`

## Launch LGSVL simulator and bridge

In the Autoware Runtime Manager, open the `Simulation` tab and click the `LGSVL simulator` button. Input the Windows simulator machine IP address and the LGSVL Simulator Launcher Port in the dialog that opens.

![LGSVL simulator bridge connection settings](https://user-images.githubusercontent.com/10348912/51304525-c599c780-1a7b-11e9-88c9-0f975d9bacc5.png)

Create a JSON configuration file using the below content and load this file from the UI by pressing the `Config` button.

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

![LGSVL simulator bridge configuration file](https://user-images.githubusercontent.com/10348912/51304799-71431780-1a7c-11e9-93cc-c9a3f652290d.png)

## Drive to make waypoints

In the Autoware Runtime Manager, enable the `waypoint_saver` setting.

Using the G29 steering wheel controller, drive simulated cars around the simulated world. Created waypoints will be saved.

# Autonomous Driving with Autoware.

Enable the following settings in the Autoware Runtime Manager for autonomous driving.

- `ndt_matching`
- `vel_pose_connect`
- `lane_rule`
- `lane_sotp`
- `lane_select`
- `obstacle_void`
- `velocity_set`
- `pure_pursuit`
- `twist_filter`
- `waypoint_loader`

The following video shows Autoware driving the simulator.

[![Autonomous driving in LGSVL demonstration video](http://img.youtube.com/vi/cBmIiR3jRvE/0.jpg)](https://www.youtube.com/watch?v=cBmIiR3jRvE&feature=youtu.be)