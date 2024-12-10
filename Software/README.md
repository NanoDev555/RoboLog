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

The Arduino and Python codes communicate using serial communication. The Arduino continuously sends sensor values to the Python program, which processes the data to control the robotic arm.

---

## Arduino Code

### Purpose

The Arduino code (`robolog.ino`) runs on the Arduino Nano 33 BLE. Its main functions are:

- **Sensor Data Acquisition**:
  - **IMU (Inertial Measurement Unit)**: Detects movements along the X and Y axes.
  - **Potentiometer**: Controls Joint 3 of the robotic arm.
  - **Gripper Button**: Toggles the gripper state (open/close).

- **Data Processing**:
  - Averages sensor readings to reduce noise.
  - Detects significant changes to decide when to send data.

- **Data Transmission**:
  - Sends processed sensor data and gripper state to the computer via serial communication.

### Key Functionality

1. **Initialization**:
   - Sets up serial communication.
   - Initializes sensors and variables.

2. **Main Loop**:
   - Reads and averages sensor data.
   - Checks for significant changes in readings.
   - Handles gripper button input with debounce logic.
   - Sends data when changes are detected.

3. **Data Format**:
   - Sends data as a comma-separated string:
     ```
     avgY,avgX,potVal,gripState
     ```
     - `avgY`: Averaged Y-axis acceleration (Joint 1).
     - `avgX`: Averaged X-axis acceleration (Joint 2).
     - `potVal`: Potentiometer value (Joint 3).
     - `gripState`: Gripper state (`0` for closed, `1` for open).

---

## Python Code

### Purpose

The Python code (`robolog_controller.py`) runs on a computer connected to the Arduino and the Niryo One robotic arm. Its main functions are:

- **Data Reception**:
  - Reads sensor data from the Arduino via serial communication.

- **Data Processing**:
  - Parses incoming data.
  - Maps sensor inputs to robot joint movements and gripper actions.

- **Robot Control**:
  - Sends movement commands to the robotic arm using the Niryo One Python API.

### Key Functionality

1. **Initialization**:
   - Connects to the Niryo One robot.
   - Sets up serial communication with the Arduino.

2. **Main Loop**:
   - Reads and parses sensor data.
   - Applies thresholds, scaling, and clamping to sensor values.
   - Controls the gripper based on button input.
   - Moves the robot joints to the calculated positions.

3. **Supporting Functions**:
   - **`map_value_to_radians()`**: Converts sensor values to joint angles.
   - **`clamp_value()`**: Ensures joint values are within allowed ranges.
   - **`toggle_gripper()`**: Opens or closes the gripper.

---

## How It Works

1. **Sensor Input**:
   - User moves the device with the Arduino and sensors.
   - IMU detects movements (Joints 1 and 2).
   - Potentiometer controls Joint 3.
   - Button toggles the gripper.

2. **Data Processing**:
   - **Arduino**: Averages readings and sends data when changes are detected.
   - **Python**: Processes data and calculates joint positions.

3. **Robot Control**:
   - Python script sends commands to the robot via the Niryo One API.
   - Robot moves joints and controls the gripper accordingly.

---

## Usage

1. **Setup**:
   - **Arduino**:
     - Upload `robolog.ino` to the Arduino Nano 33 BLE.
     - Connect sensors and gripper button.
     - Connect Arduino to the computer via USB.
   - **Niryo One Robot**:
     - Ensure the robot is powered on and connected.
   - **Python Environment**:
     - Install required Python packages: `niryo_one_python_api`, `pyserial`, `rospy`.

2. **Running the Software**:
   - Run the Python script:
     ```bash
     python robolog_controller.py
     ```

3. **Controlling the Robot**:
   - Move the Arduino device to control Joints 1 and 2.
   - Adjust the potentiometer for Joint 3.
   - Press the button to open or close the gripper.

---

## Conclusion

This documentation outlines the key aspects of the RoboLog software, focusing on the essential components to help you understand how the system operates. By understanding the Arduino and Python code functions, you can effectively work with and enhance the RoboLog project.

---

*For further details, please refer to the code comments and documentation within the source files.*
