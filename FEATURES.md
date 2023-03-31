# Our changes to various GitHub repositories

## [PX4 Autopilot](https://github.com/RETINA-UAV/PX4-Autopilot)

|                           File / Folder                          |                                 Details                                |
|:----------------------------------------------------------------:|:----------------------------------------------------------------------:|
|    init.d-posix/airframes/11234_gazebo-classic_my_iris_camera    | Airframe configuration for the `my_iris_camera` model                  |
| init.d-posix/airframes/11235_gazebo-classic_my_iris_camera_lidar | Airframe configuration for the `my_iris_camera_lidar` model            |
|               init.d-posix/airframes/CMakeLists.txt              | Modification of the CMakeLists to build the new airframe configuration |
|        simulator_mavlink/sitl_targets_gazebo-classic.cmake       | Modification of the CMakeLists to build the new models                 |

### [PX4-SITL_gazebo_classic](https://github.com/RETINA-UAV/PX4-SITL_gazebo-classic)

|     File / Folder    |                             Details                            |
|:--------------------:|:--------------------------------------------------------------:|
|      my_fpv_cam      | Our camera model                                               |
|       my_lidar       | Our 3d lidar model                                             |
|    my_iris_camera    | Our drone with the `my_fpv_cam` camera                         |
| my_iris_camera_lidar | Our drone with the `my_fpv_cam` camera and `my_lidar' 3d lidar |
|    my_world.world    | Our world                                                      |

## [Bridge PX4 - ROS / ROS2](https://github.com/RETINA-UAV/px4_ros_com)

|            File / Folder           |                                                   Details                                                   |
|:----------------------------------:|:-----------------------------------------------------------------------------------------------------------:|
| sensor_combined_listener.launch.py | We simply corrected an error in a sensor_combined_listener_node script, to test the operation of the bridge |

