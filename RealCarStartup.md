# Real Car Startup

For Autoware beginners, the minimum data and nodes for autonomous driving with real car are described. More detailed descriptions are work in progress.

# Mandatory

Data
- TF
- PointCloud Map

Sensing
- LiDAR

Localization
- voxel_grid_filter
- ndt_matching

Connector
- vel_pose_connect

Planning - Mission
- waypoint_loader
- lane_rule
- lane_stop
- lane_select
- obstacle_avoid (not for obstacle avoid)
- velocity_set

Planning - Motion
- pure_pursuit
- twist_filter

# Optional for real car

Actuation
- different for each car

<!--
Socket
- twist_gate (automatically launched by twist_filter.launch)
- vehicle_sender
- vehicle_receiver
-->

# Optional for obstacle stop

Sensing
- ray_ground_filter (or ring_round_filter)

Detection
- lidar_euclidean_cluster_detect

# Optional for real road

Data
- Vector Map

# Optional for traffic light

Sensing
- Camera

Traffic Light Recognizer
- feat_proj
- region_tlr

<!--
# Optional for localization feedback

Connector
- can2odom
-->

<!--
# Optional for localization init

Localization
- nmea2tfpose
-->