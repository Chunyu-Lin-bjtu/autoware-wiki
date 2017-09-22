# How to Calibrate Camera

## 1. Preparation for calibration

1.1　Activate the camera.<br>
　　　*Set the color and resolution same as Autoware.

1.2　Activate Velodyne.

1.3　Run Autoware.

1.4　On the Setup tag, start the TF of Baselink to Localizer.

1.5　On the Sensing tag, start the camera node of Cameras.

1.6　On the Sensing tag, start the Velodyne node of LIDARs.

1.7　On the Sensing tag, start Calibration Tool Kit or RViz and monitor camera image and<br>
　　　Velodyne point cloud image.

1.8　Check the standing position at a short distance (about 5 m).<br>
　　　Hold the checkerboard in portrait orientation ([Note:1](#note1)) and the checkerboard is completely<br>
　　　positioned at the center-lower end, center-upper end, lower-right end, upper-right end, lower-left end,<br>
　　　upper-left end position of the camera image screen (within the reach of your hand) Check<br>
　　　the range shown in the camera image and the Velodyne point cloud image.<br>
　　　It is good to set a coin on the ground for the standing position.<br>
　　　*If the camera image or Velodyne point cloud image of the checkerboard is missing, it can not be<br>
　　　　used for calibration.<br>
　　　*For accurate calibration, it is necessary to record many poses of checkerboard in the widest possible<br>
　　　　area within the camera and Velodyne's field of view.

1.9　As in the previous section, confirm the standing position at a long distance.([Note:2](#note2))<br>
　　　*If too far, accurate calibration will not be possible.

## 2. Recording ROSBAG for calibration

2.1　At the beginning, we start with the pose of near-middle-bottom and front. (see movie)<br>
　　　*In the far position, as the point clouds on the board decrease, please hide the body<br>
　　　　in the back of the board, so as not to be confused with the point cloud of the body.

2.2　In ROSBAG, start recording the topics of "/image_raw" and "/points_raw".

2.3　In total of 60 poses in the following order, stop for about 2 seconds for each pose.<br>
　　　at the near-middle-lower, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the near-middle-upper, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the near-right-lower, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the near-right-upper, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the near-left-lower, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the near-left-upper, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the far-middle-lower, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the far-middle-upper, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the far-right-lower, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the far-right-upper, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the far-left-lower, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　at the far-left-upper, front -> right tilt -> left tilt -> down tilt -> up tilt<br>
　　　Tilt the board about 30 degrees.<br>
　　　*It is not necessary to get all the poses perfectly.

2.4　Stop recording the topic of ROSBAG.

## 3. Operation of Calibration Tool Kit (with movie)

3.1　Play the ROSBAG for calibration acquired in the previous section, for a moment.<br>
　　　Pause immediately after Play.

3.2　Start Calibration Tool Kit.<br>
　　　- For "Select Input Image Topic", select "/image_raw" and press OK.<br>
　　　- For "Calibration Type", select "Camera->Velodyne" and press OK.<br>
　　　*It can start after Play->Pause ROSBAG.

3.3　To change Pattern Size and Pattern Number, after changing the value, click (X) on<br>
　　　the upper left to temporarily exit and restart the Calibration Tool Kit.<br>
　　　*The setting values of Autoware standard checkerboard are as follows.<br>
　　　　- Pattern Size： 0.108 X 0.108<br>
　　　　- Pattern Number： 6 X 8

3.4　Release Pause of the ROSBAG for a moment, and Pause again。

3.5　At large display, align the four image display panels in quarters.

　　　At small display, make the upper-left and upper-right panels larger and the lower-left and<br>
　　　lower-right panels smaller, as below.

3.6　The upper-left Camera Image Panel displays the current camera image.<br>
　　　Adjust the image position so that the checkerboard is at the center of the panel.<br>
　　　Confirm that the checkerboard is a near-center-lower-front pose, otherwise release ROSBAG Pause<br>
　　　and Pause again in the near-center-lower-front.<br>
　　　*The operation on the Camera Image Panel is as follows.<br>
　　　　- With the scrollbar or the cursor keys, the image moves vertically and horizontally.<br>
　　　　- With the mouse wheel, the image moves up and down。

3.7　The upper-right Point Cloud Image Panel shows the current Velodyne point clouds.<br>
　　　At first the view point is downward from Velodyne, so it's too low to see anything.<br>
　　　Press "↓" once to display point clouds as if Velodyne look down from above.<br>
　　　(If the background color is black, press "b" to change the background color to gray.[Note:3](#note3))

　　　*The operation in the Point Cloud Image Panel is as follows.<br>
　　　　- Viewpoint movement: ↑=forth, ↓=back, ←=left, →=right, PgUp=up, PgDn=down<br>
　　　　- Viewpoint rotation: a=left, d=right, w=up, s=dowm (q=left-tilt, e=right-tilt)<br>
　　　　- Projection mode: 1=perspective, (2=orthographic)<br>
　　　　- Point size: o=small. (p=large)<br>
　　　　- Change background color: b<br>
　　　　- Change amount of viewpoint movement: mouse wheel forward=increase, backword=decrease

　　　Key operation of viewpoint movement in Point Cloud Image Panel<br>
　　　Please release Num Lock.<br>
　　　Adjust the amount of viewpoint movement with the mouse wheel.<br>
　　　*As the viewpoint moves, the image moves in the opposite direction.

　　　Key operation of viewpoint rotation in Point Cloud Image Panel<br>
　　　*As the viewpoint rotates, the image moves in the opposite direction.。

　　　Mouse operation on Point Cloud Image Panel<br>
　　　(For point cloud extraction/cancellation, only the Captured Point Cloud Image Panel)

　　　The red, green and blue origin mark at the center of the Point Cloud Image Panel represents<br>
　　　the position and direction of Velodyne (red=forward, green=left, blue=upward).<br>
　　　Move the viewpoint to a viewable position with the following operations.<br>
　　　(1) Hold "e" and rotate so that the viewpoint is in front of the car.<br>
　　　(2) Rotate the mouse wheel backward to minimize the amount of viewpoint movement.<br>
　　　(3) Hold "↑" so that the ground can be seen at the moment.<br>
　　　　　While holding "↑", rotate the mouse wheel to adjust the moving speed.<br>
　　　(4) Hold "w" and rotate the viewpoint upwards so that you can see the point clouds on the checkerboard.<br>
　　　(5) ↑, ↓, ←, →, PgUp, PgDn, a, d, w, s key to correct the checkerboard to a viewable position.<br>
　　　　　At this time, if you adjust not only the middle-lower, but also the right, left, upper and lower<br>
　　　　　pose to the position where the checker board can be seen, the later operation becomes easy.

3.8　Press the Grab button to capture the camera image and Velodyne point clouds.<br>
　　　When fail to capture, you can cancel with the Remove button.<br>
　　　*If the checkerboard image is missing and the intersection of the checker can not be acquired,<br>
　　　　Grab can not be done.

3.9　The lower-left Grabbed Camera Image Panel displays the captured camera image.<br>
　　　A tab of "Image_0" has been created.<br>
　　　Adjust the image position so that the checkerboard is at the center of the panel.<br>
　　　Confirm that the checker intersection recognition result is displayed on the image.<br>
　　　After confirmation, make the panel smaller.<br>
　　　*The operation method of the Captured Camera Image Panel is the same as the Camera Image Panel on the upper-left.

3.10　The lower-right Grabbed Point Cloud Image Panel displays the captured Velodyne clouds.<br>
　　　A tab of "Velodyne_0" has been created.<br>
　　　When you hover the cursor over the checkerboard, a green circle and two lines are displayed.<br>
　　　One is the center axis of the circle (the line perpendicular to the circle) and the other is the<br>
　　　line parallel to the circle.<br>
　　　Here, only the center axis of the circle is important, so you can ignore the line parallel to the circle.<br>
　　　*The method of operating the Grabbed Point Cloud Image Panel is the same as the Point Cloud Image Panel on the upper-right.

3.11　Visually check that the cursor (circle) is placed at the center of the checkerboard, the circles overlap<br>
　　　in parallel with the checkerboard face, and the line perpendicular to the circle is perpendicular to the<br>
　　　checkerboard face, then left click to extract point cloud.<br>
　　　Make sure that the extracted checkerboard point clouds displayed in red are in the center of the checkerboard.<br>
　　　If extraction fails, cancel with right click and extract with left click again.<br>
　　　The diameter of the green circle is the actual size (see [※2](#annotation2)), it is a size inversely proportional<br>
　　　to the distance from the viewpoint, and displayed so as to be parallel to the point group in the circle.

3.12　Release Pause of ROSBAG and grab the remaining 29 near poses consecutively while watching the upper-left<br>
　　　Camera Image Panel and the upper right point group image panel.<br>
　　　Tabs of "Image_1-29" are created in the Grabbed Camera Image Panel at the lower-left.<br>
　　　Tabs of "Velodyne_1-29" are created in the Grabbed Point Cloud Image Panel on the lower-right.

3.13　Pause the ROSBAG once the camera image is far-center-lower-front pose.<br>
　　　Adjust the image position of the upper-left Camera Image Panel and the upper-right Point Cloud Image Panel<br>
　　　to make it easy to see.

3.14　Release Pause of ROSBAG and grab the remaining 30 far poses consecutively while watching the upper-left<br>
　　　Camera Image Panel and the upper-right Point Cloud Image Panel.<br>
　　　Tabs of "Image_30-59" are created on the Grabbed Camera Image Panel at the lower-left.<br>
　　　Tabs of "Velodyne_30-59" are created in the Grabbed Point Cloud Image Panel on the lower-right.

3.15　Stop ROSBAG.

3.16　When the display is small, expand the Grabbed Camera Image Panel at the lower-left and the<br>
　　　Grabbed Point Cloud Image Panel at the lower-right to the maximum upward.

3.17　In the same way as in Section 3.11, Velodyne_59-1 will be extracted by clicking the center point cloud of<br>
　　　the checkerboard.

3.18　After extracting all center point clouds of Velodyne_0-59, press the Calibrate button to calculate the calibration data.<br>
　　　Because it takes time to calculate, monitor the CPU load of Runtime Manager and wait for it to finish.

3.19　After calculation is completed, press the Project button.<br>
　　　Make sure that the red extracted point clouds overlap at the center of the checkerboard of each of Image_0-59<br>
　　　in the Grabbed Camera Image Panel on the lower-left.<br>
　　　If the accuracy of the overlapping position is not good, correct the position of the extraction point cloud<br>
　　　of Velodyne_0-59 of the Grabbed Point Cloud Image Panel on the lower-right, (cancel by right click,<br>
　　　and re-extract with left click), then try again Calibrate->Project.

3.20　If there is no problem, press the Save button and save the calibration result with an appropriate<br>
　　　file name (extension ".yaml" is recommended).<br>
　　　As the Save Option dialog is displayed, press "No" for "Save Camera Calibration Data ?" And "No" for<br>
　　　"Save Velodyne Calibration Data ?".

3.21　Click (X) at the top-left to exit the Calibration Tool Kit.

***

## Supplement

### <a name="note1">Note:1. About orientation with checkerboard

　In normal camera calibration, the viewing angle of the camera is large in the horizontal direction,<br>
　so use the checkerboard sideways.<br>
　In the calibration of Autoware, we calibrate the camera (high resolution) and Velodyne<br>
　(coarse resolution in the height direction) at the same time.<br>
　In order to improve accuracy, it is necessary to calibrate at a long distance as much as possible,<br>
　so a certain size is required for the checkerboard.<br>
　For Autoware, we recommend A0 size (841 x 1189 mm) board for ease of acquisition and creation.

　And a vertical hold is to make it easier to hold the board, make it easier to hide the body behind the board,<br>
　to reduce Velodyne's scan line projected on the board when tilting the board back and forth.

　Checker pattern reference URL:<br>
　　<http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration?action=AttachFile&do=view&target=check-108.pdf>

### <a name="note2">Note:2. About the theoretical maximum distance between Velodyne and the checkerboard

　Grasping the position of the checkerboard with Calibration Tool Kit is done by the following method.<br>
　　- For camera images, automatic detection of checker pattern.<br>
　　- In the Velodyne point cloud image, a manual click on the Grabbed Point Cloud Image Panel.<br>

　In the Grabbed Point Cloud Image Panel, at least two Velodyne scanlines must be included in<br>
　the green circle displayed on the panel in order to be able to click and position input possible.<br>
　With only one line, the green circle can not be correctly displayed on the checkerboard surface<br>
　because the surface can not be determined.

　　　The worst case is when the scanline is in the center of the green circle. (see left figure)<br>
　　In this case, if there is no next scanline within half the diameter of the circle,<br>
　　it will not be detected as a plane.<br>
　　Condition that at least two scanlines are included: half of the circle diameter > interval of scanline

　The diameter of the green circle for extracting point cloud is the smaller of the following:<br>
　　- Pattern Size (m) [width] × Pattern Number [column]<br>
　　- Pattern Size (m) [height] × Pattern Number [row]<br>
　And with standard checkerboard of Autoware:<br>
　　・Pattern Size [width/height] = 0.108 [m]<br>
　　・Pattern Number [column] = 6<br>
　So, the diameter of the circle is:<br>
　　0.108 × 6 = 0.648 [m]<br>
　And the maximum of scan interval for always containing two Velodyne scanlines in this circle is:<br>
　　0.648/2 = 0.324 [m]<br>

　Therefore, the maximum distance between Velodyne and checkerboard is:<br>
　　maximum distance = 0.324 / tan(interval angle of vertical scan)<br>

|Model number|Vertical scan number|V. scan range[deg]|V. scan interval[deg]|Max distance[m]|
|---|:-:|:-:|:-:|:-:|
|HDL-64e|64|26.8|0.425|43.7|
|HDL-32e|32|41.3|1.332|13.9|
|VLP-16(30)|16|30|2|9.3|
|VLP-16(20)|16|20|1.333|13.9|

　In addition, when the board is tilted back and forth, the circle deforms so as to be parallel<br>
　to the board, so the apparent circle height seen from Velodyne decreases according to the tilt of the board.<br>
　For example, the minor axis when tilted 30 degree back and forth is:<br>
　　0.648×cos(30 [deg]) = 0.561 [m]<br>
　In this ellipse, two scan lines are always included, the maximum value of Velodyne's scan interval is:<br>
　　0.561/2 = 0.281 [m]<br>

　Therefore, the maximum distance from Velodyne is:<br>
　　maximum distance = 0.281 / tan(interval angle of vertical scan)<br>

|Model number|Vertical scan number|V. scan range[deg]|V. scan interval[deg]|Max distance[m]|
|---|:-:|:-:|:-:|:-:|
|HDL-64e|64|26.8|0.425|37.9|
|HDL-32e|32|41.3|1.332|12.1|
|VLP-16(30)|16|30|2|8.0|
|VLP-16(20)|16|20|1.333|12.1|

### <a name="note3">Note:3. How to make the initial background color of the Point Cloud Panel gray

　The initial background color of the Point Cloud Image Panel at the upper-right and the<br>
　Grubbed Point Cloud Image Panel at the lower-right is black, and it is not appropriate to see the point cloud.<br>
　By changing the source code of Autoware, and by catkin_make_release, you can make<br>
　the initial background color gray.

　Modify line 45 of Autoware/ros/src/util/packages/RobotSDK/glviewer/GLViewer/glviewer.cpp<br>
　　- cameraparameters.background=Eigen::Vector4d(0,0,0,1);<br>
　　+ cameraparameters.background=Eigen::Vector4d(0.5,0.5,0.5,1);

