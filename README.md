# RETINA-UAV 

Real-time Enhanced Target Identification and Navigation Assistance

## How to install

See [INSTALL.md](INSTALL.md).

## Quick start

```bash
./scripts/run_simulator.sh
```

```bash
./scripts/run_bridge_px4_ros2.sh
```

## Setup the Unity-ROS2 bridge

You can find the Unity-ROS2 bridge used is just [here](https://github.com/RobotecAI/ros2-for-unity) from the RobotecAI repository.

We've used the released version [1.1.0](https://github.com/RobotecAI/ros2-for-unity/releases/tag/1.1.0)

To make it all work you need to open a terminal, source your ros '.bash' file and lauch the unity project from the terminal.

```shell
source /opt/ros/foxy/setup.bash

cd [Path to the repo]/WorldUnity

[Unity install path]/[Unity version]/Editor/Unity -projectPath "$(pwd)"
```

