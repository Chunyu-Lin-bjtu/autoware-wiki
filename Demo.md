Please checkout the release version 1.7.0 for this demo.

`$ git checkout tags/1.7.0`

Launch files for Quick Start are moved to [Autoware/docs/quick_start](https://github.com/CPFL/Autoware/tree/master/docs/quick_start) from version 1.7.0.

## Demo data

This demo will require 3D map and ROSBAG data. Please download the following sample demo data before running the demo.

1. Download the sample 3D pointcloud/vector map data. [[link](https://www.autoware.ai/sample/sample_moriyama_data.tar.gz)]

`$ wget http://db3.ertl.jp/autoware/sample_data/sample_moriyama_data.tar.gz

1. Download the sample ROSBAG data (**LiDAR**: VELODYNE HDL-32E, **GNSS**: JAVAD GPS RTK Delta 3).  [[link](https://www.autoware.ai/sample/sample_moriyama_150324.tar.gz)]

`$ wget http://db3.ertl.jp/autoware/sample_data/sample_moriyama_150324.tar.gz

#### Want more data?

Once the demo goes well, you can visit [ROSBAG STORE](https://rosbag.tier4.jp) to get more data. Please also consider your contribution to this data sharing service by uploading your ROSBAG data.

## Demo run

Autoware provide a set of the preinstalled roslaunch scripts for the demo. Please follow the steps below:

1. Go to the Simulation tab of Autoware Runtime Manager, and load the sample ROSBAG data.

1. Play the loaded ROSBAG data, and immediately pause it once.

1. Launch RViz.

1. Go to the Quick Start tab of Autoware Runtime Manager, and load the preinstalled roslaunch scripts one by one.

Please follow the instruction video below:

[![Quick Start](http://img.youtube.com/vi/OWwtr_71cqI/mqdefault.jpg)](https://www.youtube.com/watch?v=OWwtr_71cqI)