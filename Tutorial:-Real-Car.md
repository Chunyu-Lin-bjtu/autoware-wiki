The minimum data and nodes for autonomous driving with a real car are described. Some typical options are also listed. You should select what you need, and should **make risk assessment** based on your purpose. More detailed descriptions are work in progress.

# Mandatory

This mandatory components make a car run on a given way points. The behavior of the car is controlled only by the given data and the results of localization. It can not deal with external actions.

Data
- TF
- Point Cloud Map
- Way Points

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
- different for each car type

<!--
# For ZMP Cars

Socket
- twist_gate (automatically launched by twist_filter.launch)
- vehicle_sender
- vehicle_receiver
-->

# Obstacle Stop

With this option, the car can stop short of obstacles on way points. If the obstacles are removed, the car starts running again.

Sensing
- ray_ground_filter (or ring_round_filter)

# Real Road

With this option, the car can run on real road without traffic light. Cross walk, stop line, or etc, included in the data can be considered.

Data
- Vector Map

# Traffic Light

With this option, the car can stop when the traffic light is red.

Data
- Vector Map

Sensing
- Camera

Traffic Light Recognizer
- feat_proj
- region_tlr

# For Localization Feedback

Connector
- can2odom

<!--
# For Localization Init

Localization
- nmea2tfpose
-->
