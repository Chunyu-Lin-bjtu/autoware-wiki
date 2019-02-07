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
- autoware_sensor_msgs

## Topic Name

/detection/ParentComponent/DataName

Examples:
- /detection/lidar_detector/objects
- /detection/image_detector/objects
- etc...

## A Motif

![A Motif](https://user-images.githubusercontent.com/38030772/46925660-0393e380-d068-11e8-8b75-2f0586f20a17.png)