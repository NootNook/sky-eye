# INSTALLATION

Testing of Ubuntu 20.04 and ROS 2 Foxy

## ROS 2 FOXY

https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

## EASY WAY

```bash
./scripts/install.sh
```

## INSTALLATION DETAIL

### PX4 ROS Com and PX4 msg

```bash
cd modules/px4_ros_com_ros2
colcon build
```

### Micro-ROS-Agent

```bash
cd modules/microros_ws
colcon build
source install/local_setup.sh
ros2 run micro_ros_setup create_agent_ws.sh
ros2 run micro_ros_setup build_agent.sh
```