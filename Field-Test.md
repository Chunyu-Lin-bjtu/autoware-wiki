One of the significant advantages of Autoware is that you can start field testing of your self-driving vehicle _within a day_ once a 3D LiDAR sensor is mounted on the vehicle. You can build a 3D map, make a route, and follow it autonomously, using Autoware. To go beyond, you would also need cameras and a professional 3D map with a full set of Autoware modules. For the first time of field testing, however, you can begin with the following simple test.

## To Begin With

### Build a pointcloud map

Autoware provides a 3D mapping module based on simultaneous localization and mapping (SLAM). It builds a local-coordinate pointcloud map while manually driving the vehicle. You should be careful about a loop closure constraint. If you drive too far from the origin, the resulting pointcloud map might be misaligned with the real geographical features, unless you use the Graph SLAM method. That is, the pointcloud map built by Autoware alone should not be large-scale.

### Make a route in the pointcloud map

Once the pointcloud map is ready, you can make a route that you want to follow autonomously. The most straightforward way to make a route is that you drive manually once on the route and record vehicle positions on a time. This trace of vehicle positions can be saved as _waypoints_. All you have to do is to follow these waypoints. A more intelligent way, on the other hand, is that you use [VectorMapper](https://maptools.tier4.jp/vector_mapper_description/) to add road features to the pointcloud map, and follow the waypoints comprising the center line of the lane of your route; however this is a time-consuming task.

### Follow waypoints of the route

Once you make a route with waypoints, all you have to do is just to follow these waypoints, controlling the speed/throttle and the angle/steering based on the localization and detection results. To go beyond, for example on a public road, you would need to activate more modules, such as the object tracker, traffic light recognizer, and decision maker. You also suppose that, in practice, the waypoints is generated by some high-accuracy navigation service, which will be supported on [Autoware.AI](https://www.autoware.ai). Once the waypoints are ready, the exercise you try herein will be useful in any test field.

## To Go Beyond

### Public Road Testing
[![Public Road Demonstration](http://img.youtube.com/vi/5DaQBZvZwAI/mqdefault.jpg)](https://www.youtube.com/watch?v=5DaQBZvZwAI)

### Private Course Testing
[![Test Field Demonstration](http://img.youtube.com/vi/zujGfJcZCpQ/mqdefault.jpg)](https://www.youtube.com/watch?v=zujGfJcZCpQ)