Design is important for readability and maintainability. It is highly recommended to follow the design rules for distributing your idea. The outline is based on [the overview](https://github.com/CPFL/Autoware/wiki/Overview).

# Namespace

## Message Type

autoware_(namespace)_msgs::typename

Examples:
- autoware_detection_msgs
- autoware_localization_msgs
- autoware_prediction_msgs
- autoware_intelligence_msgs
- autoware_state_msgs
- autoware_mission_msgs
- autoware_motion_msgs

## Topic Name

/namespace/ParentComponent_DataName

Examples:
- /detection/vision_objects
- /detection/lidar_objects
- /detection/detected_objects
- /detection/tracked_objects

## A Motif

![A Motif](https://user-images.githubusercontent.com/38030772/43500108-dbe7a948-9589-11e8-80c7-8c5c307eabe6.png)
