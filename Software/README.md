# RoboLog Software Documentation

## Introduction

This document provides an overview of the software components of the RoboLog project. It explains the functionality of both the Arduino and Python code that work together to control the Niryo One robotic arm using sensor inputs. Each code section has its own table of contents for easy navigation.

## Table of Contents

- [Arduino Code](#arduino-code)
  - [Purpose](#arduino-purpose)
  - [Key Functionality](#arduino-key-functionality)
- [Python Code](#python-code)
  - [Purpose](#python-purpose)
  - [Key Functionality](#python-key-functionality)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Conclusion](#conclusion)

---

## Arduino Code

### Purpose

The **Arduino code** (`robolog.ino`) runs on the Arduino Nano 33 BLE. Its main purposes are:

- **Sensor Data Acquisition**: Reads data from:
  - **IMU (Inertial Measurement Unit)**: Built-in sensor to detect movements along the X and Y axes.
  - **Potentiometer**: External sensor to control Joint 3 of the robotic arm.
  - **Button for Gripper Control**: External button to toggle the gripper state (open/close).

- **Data Processing**:
  - Averages sensor readings to reduce noise.
  - Detects significant changes in sensor inputs.

- **Data Transmission**:
  - Sends processed sensor data and gripper state to the computer via serial communication.

### Key Functionality

#### Initialization (`setup()`)

- Starts serial communication at 115200 baud.
- Initializes sensor reading arrays for averaging IMU data.
- Sets pin modes for the potentiometer and gripper button.
- Initializes the IMU and verifies successful startup.

#### Main Loop (`loop()`)

- Implements non-blocking timing to sample sensor data at regular intervals.
- Reads and averages IMU acceleration data along the X and Y axes.
- Reads potentiometer value for Joint 3 control.
- Checks for significant changes in sensor readings compared to previous values.
- Handles gripper button presses with debounce logic.
- Sends updated sensor data and gripper state over serial communication when changes are detected.

#### Data Transmission (`printData()`)

- Formats and sends the sensor data and gripper state as a comma-separated string:


- `avgY`: Averaged Y-axis acceleration (controls Joint 1).
- `avgX`: Averaged X-axis acceleration (controls Joint 2).
- `potVal`: Potentiometer value (controls Joint 3).
- `gripState`: Gripper state (`0` for closed, `1` for open).

---

## Python Code

### Purpose

The **Python code** (`robolog_controller.py` and supporting modules) runs on a computer connected to the Arduino and the Niryo One robotic arm. Its main purposes are:

- **Data Reception**:
- Establishes serial communication with the Arduino to receive sensor data.

- **Data Processing**:
- Parses and processes the incoming sensor data.
- Maps sensor inputs to corresponding joint movements and gripper actions.

- **Robot Control**:
- Uses the Niryo One Python API to send movement commands to the robotic arm based on sensor inputs.

### Key Functionality

#### Initialization

- **Connects to the Niryo One Robot**:
- Initializes a ROS node.
- Attempts to establish a connection with the Niryo One robot.
- Selects the appropriate tool (Gripper 1).

- **Sets Up Serial Communication**:
- Opens a serial connection to the Arduino at the specified port and baud rate.

#### Main Loop

- **Reads Sensor Data**:
- Continuously reads data from the Arduino via serial communication.
- Parses the comma-separated string into individual sensor values:
  - `y_accel`: Averaged Y-axis acceleration (controls Joint 1).
  - `x_accel`: Averaged X-axis acceleration (controls Joint 2).
  - `pot_value3`: Potentiometer value (controls Joint 3).
  - `button_state`: Gripper state (`0` for closed, `1` for open).

- **Processes Sensor Data**:
- **Thresholding**:
  - Applies thresholds to determine if the change in sensor data is significant enough to warrant movement.
- **Scaling and Clamping**:
  - Scales IMU acceleration values with a scaling factor.
  - Clamps joint values within their minimum and maximum ranges.

- **Controls the Robot**:
- **Gripper Control**:
  - Toggles the gripper state based on the `button_state` value.
- **Joint Movement**:
  - Moves Joints 1, 2, and 3 to the calculated positions.
  - Sets the robot's arm velocity for smoother movements.

#### Supporting Functions

- **`connect_to_robot()`**:
- Handles the connection to the Niryo One robot, with retries upon failure.

- **`select_tool()`**:
- Selects the gripper tool on the robot.

- **`map_value_to_radians()`**:
- Maps potentiometer values to joint angles in radians.

- **`clamp_value()`**:
- Ensures joint values stay within their allowed ranges.

- **`toggle_gripper()`**:
- Opens or closes the gripper based on the input state.

- **`move_joints_to_final_position()`**:
- Calculates joint positions from sensor data and commands the robot to move.

---

## How It Works

1. **Sensor Input**:
 - The user moves the device containing the Arduino Nano 33 BLE and attached sensors.
 - IMU detects movements along the X and Y axes (Joints 1 and 2).
 - Potentiometer provides input for Joint 3.
 - Button toggles the gripper state.

2. **Data Processing on Arduino**:
 - Arduino collects and averages sensor readings.
 - Detects significant changes to decide when to send data.
 - Sends processed data over serial communication.

3. **Data Processing on Computer**:
 - Python script reads incoming sensor data from the Arduino.
 - Processes data to calculate desired joint positions and gripper actions.
 - Applies thresholds, scaling, and clamping to sensor values.

4. **Robot Control**:
 - Python script sends movement commands to the Niryo One robot via the API.
 - Robot moves joints to specified positions, mimicking user's movements.
 - Gripper opens or closes based on user input.

---

## Usage

1. **Setup**:
 - **Arduino**:
   - Upload the `robolog.ino` sketch to the Arduino Nano 33 BLE.
   - Connect sensors and gripper button as per the code requirements.
   - Connect the Arduino to the computer via USB.
 - **Niryo One Robot**:
   - Ensure the robot is powered on and connected to the network.
 - **Python Environment**:
   - Install required Python packages: `niryo_one_python_api`, `serial`, `rospy`.

2. **Run the Python Script**:
 - Open a terminal and navigate to the directory containing the Python script.
 - Run the script:
   ```bash
   python robolog_controller.py
   ```
 - The script will attempt to connect to the Niryo One robot and set up serial communication with the Arduino.

3. **Control the Robot**:
 - **Joints 1 and 2**:
   - Move the Arduino device to control the robot's base rotation and shoulder movement.
 - **Joint 3**:
   - Adjust the potentiometer to control the elbow joint.
 - **Gripper**:
   - Press the button to open or close the gripper.

---

## Conclusion

This software enables real-time control of the Niryo One robotic arm using sensor inputs from an Arduino Nano 33 BLE. By understanding the functionality of both the Arduino and Python code, future developers can maintain and enhance the RoboLog project to achieve more sophisticated control and features.

---

*Note: For any questions or further assistance, please refer to the code comments and documentation within the source files.*

