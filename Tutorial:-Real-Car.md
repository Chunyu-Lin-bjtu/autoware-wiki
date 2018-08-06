The minimum data and nodes for autonomous driving with real car are described. More detailed descriptions are work in progress.

# Mandatory

Data
- TF
- Point Cloud Map

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

Actuation
- different for each car

<!--
# For ZMP Cars

Socket
- twist_gate (automatically launched by twist_filter.launch)
- vehicle_sender
- vehicle_receiver
-->

# For Obstacle Stop

Sensing
- ray_ground_filter (or ring_round_filter)

Detection
- lidar_euclidean_cluster_detect

# For Real Road

Data
- Vector Map

# For Traffic Light

Sensing
- Camera

Traffic Light Recognizer
- feat_proj
- region_tlr

<!--
# Optional for Localization Feedback

Connector
- can2odom
-->

<!--
# Optional for Localization Init

Localization
- nmea2tfpose
-->