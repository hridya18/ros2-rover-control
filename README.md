# ROS 2 Autonomous Rover Decision Suite

A lightweight, modular ROS 2 Jazzy workspace package implementing a publisher/subscriber topology to simulate a basic autonomous rover obstacle avoidance mechanism.

## Architecture Overview
The system splits hardware telemetry logic from decision routing across two concurrent Python nodes:
* **Sensor Simulator Node (`sensor_simulator.py`)**: Acts as a publisher, generating mock float streams simulating distance readings over the `sensor/distance` topic.
* **Rover Brain Node (`rover_brain.py`)**: Acts as a subscriber parsing telemetry inputs, broadcasting automated safety decisions onto a `motor/command` topic.

## How to Run
```bash
# Navigate to workspace root
cd ~/ros2_ws

# Compile the packages
colcon build

# Source environment variables
source install/setup.bash

# Terminal 1: Spin up the Decision Controller
ros2 run rover_control brain

# Terminal 2: Run the environment telemetry generator
ros2 run rover_control sensor
\`\`\`
