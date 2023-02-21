#!/bin/bash

if [ -n "$ZSH_VERSION" ]; then
  source "$(pwd)"/modules/microros_ws/install/local_setup.zsh
else
  source "$(pwd)"/modules/microros_ws/install/local_setup.bash
fi

ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888