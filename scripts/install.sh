#!/bin/bash

./modules/PX4-Autopilot/Tools/setup/ubuntu.sh --no-nuttx

(cd modules/px4_ros_com_ros2 && colcon build)
(cd modules/microros_ws && colcon build)

if [ -n "$ZSH_VERSION" ]; then
  source "$(pwd)"/modules/microros_ws/install/local_setup.zsh
else
  source "$(pwd)"/modules/microros_ws/install/local_setup.bash
fi

ros2 run micro_ros_setup create_agent_ws.sh
ros2 run micro_ros_setup build_agent.sh