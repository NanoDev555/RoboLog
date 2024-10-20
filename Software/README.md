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
