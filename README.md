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

## Goal of the project

Our project, called RETINA - UAV, is an acronym for "Real-time Enhanced Target Identification and Navigation Assistance - Unmanned Aerial Vehicle". The goal of this project is to help rescuers locate and save people in danger in a conflict zone while detecting certain dangers such as armed vehicles or others. To do this, users will wear augmented reality glasses to visualize all the detections made by the drone. These detections will be marked by the time and distance at which they were made relative to the user.

To better understand the project's functioning, here are the steps:
Firstly, the operator selects the GPS area where they want to send the drone from a ground control station.
Secondly, the drone heads towards the selected area and performs surveillance by detecting everything it can. During its mission, it uses its LiDAR sensor to reconstruct the environment in a 3D simulation. Then, the drone combines the 3D reconstruction data with the detections made to place them in the created virtual world. Thanks to this, a map of the area can be viewed by operators. The user of the augmented reality glasses can also visualize all the detections made through them, even through walls and different obstacles. With all this information, rescuers can be more effective in their operations.
