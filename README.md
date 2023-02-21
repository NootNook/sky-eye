# RETINA-UAV 
## Real-time Enhanced Target Identification and Navigation Assistance

# Setup the Unity-ROS2 bridge

You can find the Unity-ROS2 bridge used is just [here](https://github.com/RobotecAI/ros2-for-unity) from the RobotecAI repository.

We've used the released version [1.1.0](https://github.com/RobotecAI/ros2-for-unity/releases/tag/1.1.0)

To make it all work you need to open a terminal, source your ros '.bash' file and lauch the unity project from it unless it will not work.

```shell
source /opt/ros/foxy/setup.bash

cd [Path to the repo]/WorldUnity

[Unity install path]/[Unity version]/Editor/Unity -projectPath "$(pwd)"
```

