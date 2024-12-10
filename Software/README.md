# RoboLog Software Documentation

## Introduction

This document provides an overview of the software components of the RoboLog project. It focuses on explaining the functionality of the Arduino and Python code that work together to control the Niryo One robotic arm using sensor inputs.

## Table of Contents

- [Overview](#overview)
- [Arduino Code](#arduino-code)
- [Python Code](#python-code)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Conclusion](#conclusion)

---

## Overview

The RoboLog project aims to control a Niryo One robotic arm using sensor inputs from an Arduino Nano 33 BLE. The software consists of:

- **Arduino Code**: Reads sensor data and sends it to the computer.
- **Python Code**: Processes sensor data and controls the robotic arm.

The Arduino and Python programs communicate via serial communication. The Arduino continuously sends sensor values to the Python script, which processes the data to control the robot arm. Below are examples of how data is transmitted:

### Arduino Example:
```cpp
Serial.print(medelY);
Serial.print(',');
Serial.print(medelX);
Serial.print(',');
Serial.print(potVärde);
Serial.print(',');
Serial.println(gripTillstånd);
```
## Arduino Code

### Purpose

The Arduino code (`robolog.ino`) runs on the Arduino Nano 33 BLE. Its primary functions are:

1. **Sensor Data Acquisition**:
   - Reads data from an IMU for Joint 1 and Joint 2.
   - Uses a potentiometer for Joint 3.
   - Detects gripper button presses.

2. **Data Processing**:
   - Averages sensor readings to minimize noise.
   - Detects significant changes to trigger data transmission.

3. **Data Transmission**:
   - Sends sensor values and gripper state to the computer as a comma-separated string:
     ```
     avgY,avgX,potVal,gripState
     ```

### Key Functionality

1. **Initialization**:
   - Sets up serial communication.
   - Initializes sensors and variables.

2. **Main Loop**:
   - Reads sensor data and averages values.
   - Detects changes and sends the formatted string via serial communication.

---

## Python Code

### Purpose

The Python code (`robolog_controller.py`) processes sensor data and controls the Niryo One robotic arm. Its main functions include:

1. **Data Reception**:
   - Reads serial data from the Arduino.

2. **Data Processing**:
   - Parses the incoming data and applies scaling, clamping, and mapping to calculate joint positions.

3. **Robot Control**:
   - Sends joint movement commands to the Niryo One robot via its Python API.
   - Controls the gripper based on button input.

### Key Functionality

1. **Initialization**:
   - Connects to the Niryo One robot.
   - Sets up serial communication with the Arduino.

2. **Main Loop**:
   - Continuously reads data from the serial port.
   - Processes and maps the values to robot movements and gripper control.

3. **Supporting Functions**:
   - **`map_value_to_radians()`**: Converts sensor values to joint angles.
   - **`clamp_value()`**: Ensures joint values are within allowed ranges.
   - **`toggle_gripper()`**: Opens or closes the gripper.

---

## How It Works

1. **Sensor Input**:
   - Users interact with the Arduino device.
   - IMU values control Joints 1 and 2.
   - Potentiometer adjusts Joint 3.
   - Button toggles the gripper state.

2. **Data Transmission**:
   - **Arduino**: Detects changes and sends them via serial communication.
   - **Python**: Processes received data and sends robot control commands.

3. **Robot Execution**:
   - The Niryo One robot executes joint movements and gripper actions.

---

## Usage

### Requirements
- **Arduino**: Nano 33 BLE with connected IMU, potentiometer, and button.
- **Python Environment**:
  - Required libraries: `niryo_one_python_api`, `pyserial`, `rospy`.
- **Niryo One Robot**: Ensure the robot is connected and operational.

### Steps

1. **Setup**:
   - Upload the `robolog.ino` file to the Arduino.
   - Connect the Arduino to the computer.
   - Power on the Niryo One robotic arm.

2. **Run the Python Script**:
   - Execute the Python controller:
     ```bash
     python robolog_controller.py
     ```

3. **Control the Robot**:
   - Move the Arduino device for Joints 1 and 2.
   - Adjust the potentiometer for Joint 3.
   - Press the button to toggle the gripper.

---

## Conclusion

The RoboLog project integrates Arduino and Python to achieve efficient robotic arm control using sensor inputs. By processing sensor data in real-time, the system ensures precise joint movements and gripper actions. This documentation provides a comprehensive overview to help developers understand and enhance the RoboLog system.

---

*For further details, refer to the comments in the source code files.*
