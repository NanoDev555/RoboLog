# RoboLog Software Documentation

## Introduction

This document provides an overview of the software component of the RoboLog project. The focus is on explaining the functionality of the code and how it controls the prosthetic arm using sensor inputs.

## Code Functionality

The software consists of two main parts:

1. **Arduino Code (`robolog.ino`):** Runs on the Arduino Nano 33 BLE and is responsible for reading sensor inputs and sending processed data to the computer.

2. **Python Scripts (`robolog_controller.py` and supporting modules):** Run on a computer to receive sensor data from the Arduino, process it, and control the Niryo One robotic arm accordingly.

### Arduino Code (`robolog.ino`)

**Purpose:**

- Read data from the following sensors:
  - **IMU (Inertial Measurement Unit):** Built-in sensor used to detect movements along the X and Y axes.
  - **Potentiometer:** External sensor used to control Joint 3 of the robotic arm.
  - **Button for Gripper Control:** External button used to toggle the gripper state (open/close).

- Process and filter sensor data to reduce noise and improve accuracy.

- Detect significant changes in sensor readings to determine when to send data.

- Send the processed sensor data and gripper state to the computer via serial communication.

**Key Functionality:**

- **Initialization (`setup()`):**
  - Starts serial communication at 115200 baud.
  - Initializes sensor reading arrays for averaging IMU data.
  - Sets pin modes for the potentiometer and gripper button.
  - Initializes the IMU and checks for successful startup.

- **Main Loop (`loop()`):**
  - Implements a non-blocking timing mechanism to sample sensor data at regular intervals without delaying other processes.
  - Reads IMU acceleration data along the X and Y axes.
  - Averages multiple readings to smooth out the data.
  - Reads the potentiometer value for Joint 3 control.
  - Checks for significant changes in sensor readings compared to previous values.
  - Handles gripper button presses with debounce logic to prevent false triggers.
  - Sends updated sensor data and gripper state over serial communication when changes are detected.

- **Data Transmission (`printData()`):**
  - Formats and sends the sensor data (average Y, average X, potentiometer value) and gripper state as a comma-separated string over serial communication.

### Python Code (`robolog_controller.py`)

**Purpose:**

- Establish serial communication with the Arduino to receive sensor data.

- Process incoming sensor data to map it to corresponding joint movements and gripper actions.

- Use the Niryo One Python API to send movement commands to the robotic arm based on the sensor inputs.

**Key Functionality:**

- **Sensor Data Handling:**
  - Reads incoming serial data from the Arduino.
  - Parses the comma-separated string into individual sensor values:
    - `avgY`: Averaged Y-axis acceleration (controls Joint 1).
    - `avgX`: Averaged X-axis acceleration (controls Joint 2).
    - `potVal`: Potentiometer value (controls Joint 3).
    - `gripState`: Gripper state (`0` for closed, `1` for open).

- **Data Processing (`process_sensor_data()`):**
  - Converts sensor readings into appropriate joint positions using scaling factors.
  - Maps the sensor inputs to joint angles for the robotic arm.

- **Robot Control:**
  - Sends joint movement commands to the Niryo One robot using the processed joint positions.
  - Controls the gripper state by sending open or close commands based on the `gripState` value.

- **Main Loop:**
  - Continuously reads sensor data and updates the robot's movements and gripper state in real-time.

## How It Works

1. **Sensor Input:**
   - The user moves the device containing the Arduino Nano 33 BLE and attached sensors.
   - The IMU detects movements along the X and Y axes, representing motions for Joints 1 and 2.
   - The potentiometer provides input for Joint 3, allowing manual adjustment.
   - The button allows the user to toggle the gripper's open or closed state.

2. **Data Processing on Arduino:**
   - The Arduino collects and averages sensor readings to reduce noise.
   - It detects significant changes in sensor inputs to decide when to send data.
   - The Arduino sends the processed data to the computer over serial communication.

3. **Data Processing on Computer:**
   - The Python script reads the incoming sensor data.
   - It processes the data to calculate the desired joint positions.
   - It translates the `gripState` into gripper commands.

4. **Robot Control:**
   - The Python script uses the Niryo One Python API to send movement commands to the robotic arm.
   - The robot moves its joints to the specified positions, mimicking the user's movements.
   - The gripper opens or closes based on the user's input.

## Usage

1. **Setup:**
   - Upload the `robolog.ino` sketch to the Arduino Nano 33 BLE.
   - Connect the Arduino to the computer via USB.
   - Ensure the Niryo One robot is powered on and connected to the network.

2. **Run the Python Script:**
   - Navigate to the directory containing `robolog_controller.py`.
   - Run the script:
     ```bash
     python3 robolog_controller.py
     ```
   - The script will start reading sensor data and controlling the robot accordingly.

3. **Control the Robot:**
   - Move the device containing the Arduino to control Joints 1 and 2.
   - Adjust the potentiometer to control Joint 3.
   - Press the button to toggle the gripper state.

## Conclusion

This software enables real-time control of the Niryo One robotic arm using sensor inputs from an Arduino Nano 33 BLE. By understanding the code functionality and how it processes sensor data to control the robot, future developers can further develop and enhance the RoboLog project.

---

*Note: For any questions or further assistance, please refer to the code comments and documentation within the source files.*

