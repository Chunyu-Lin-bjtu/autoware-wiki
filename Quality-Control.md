
# Common Build Flags
[autoware_build_flags](https://github.com/CPFL/Autoware/tree/develop/ros/src/common/cmake/autoware_build_flags) controls the build flags of the entire components in Autoware. If a new package is added into Autoware, please use it as shown in the following examples.

## package.xml
```diff
  <license>Apache 2</license>
  <buildtool_depend>catkin</buildtool_depend>
+ <buildtool_depend>autoware_build_flags</buildtool_depend>
```

## CMakeLists.txt
```diff
find_package(
        catkin REQUIRED COMPONENTS
+       autoware_build_flags
```
There is no need to add `-std=c++11` because autoware_build_flags inserts it automatically.
