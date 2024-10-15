# RoboLog Hardware Documentation

## Introduction

This document provides detailed information about the hardware components used in the RoboLog project. It is intended for future developers who will take over the project next year, helping them understand the role and integration of each hardware part.

## Table of Contents

1. [Overview](#overview)
2. [Hardware Components](#hardware-components)
   - [Niryo One Robot](#niryo-one-robot)
   - [Arduino Nano 33 BLE](#arduino-nano-33-ble)
   - [Sensors](#sensors)
     - [Inertial Measurement Unit (IMU)](#inertial-measurement-unit-imu)
     - [Potentiometer](#potentiometer)
     - [Flex Sensor](#flex-sensor)
   - [Connections and Wiring](#connections-and-wiring)
   - [Power Supply](#power-supply)
3. [Setup and Assembly](#setup-and-assembly)
4. [Troubleshooting](#troubleshooting)
5. [Maintenance](#maintenance)
6. [Future Improvements](#future-improvements)
7. [References](#references)

## Overview

The RoboLog project aims to develop a prosthetic arm controlled through various sensor inputs to mimic natural human movements. The hardware setup includes a Niryo One robotic arm, an Arduino Nano 33 BLE microcontroller, and several sensors that capture user input.

## Hardware Components

### Niryo One Robot

#### Description

The **Niryo One** is a 6-axis collaborative robotic arm designed for education and research. It is powered by ROS (Robot Operating System) and allows for advanced programming and control.

#### Specifications

- **Degrees of Freedom**: 6
- **Payload**: Up to 0.5 kg
- **Reach**: 440 mm
- **Software Compatibility**: ROS, Python APIs
- **End Effectors**: Gripper, vacuum pump, electromagnet (the gripper is used in this project)

#### Role in the Project

The Niryo One serves as the physical prosthetic arm, executing movements based on sensor input. It mimics the natural motion of a human arm by responding to real-time data from the sensors.

### Arduino Nano 33 BLE

#### Description

The **Arduino Nano 33 BLE** is a compact microcontroller board featuring Bluetooth Low Energy connectivity and an onboard IMU.

#### Features

- **Microcontroller**: nRF52840 (ARM Cortex-M4 CPU)
- **Operating Voltage**: 3.3V
- **Digital I/O Pins**: 14
- **Analog Input Pins**: 8
- **Connectivity**: Bluetooth 5.0 BLE
- **Sensors**: 9-axis IMU (LSM9DS1)

#### Role in the Project

The Arduino Nano 33 BLE collects data from the connected sensors (IMU, potentiometer, flex sensor) and sends this data to the control software running on a computer, which then commands the Niryo One robot.

### Sensors

#### Inertial Measurement Unit (IMU)

##### Description

The IMU is a 9-axis sensor combining an accelerometer, gyroscope, and magnetometer, allowing for motion tracking and orientation detection.

##### How It's Used

- **Motion Capture**: Detects the orientation and movement of the user's limb.
- **Data Output**: Provides roll, pitch, and yaw angles used to control corresponding joints on the Niryo One.

#### Potentiometer

##### Description

A potentiometer is a three-terminal resistor with a sliding contact that forms an adjustable voltage divider.

##### How It's Used

- **Manual Control**: Allows the user to adjust the position of a specific joint on the robot manually.
- **Data Output**: Provides variable resistance translated into position values for the robot's joint.

#### Flex Sensor

##### Description

A flex sensor changes its resistance based on the amount it is bent.

##### How It's Used

- **Gripper Control**: Bending the flex sensor controls the opening and closing of the robot's gripper.
- **Data Output**: Resistance values correspond to the degree of bend, which are mapped to gripper positions.

### Connections and Wiring

#### Schematic Diagrams

*Please insert diagrams here if available.*

#### Pin Connections

- **Arduino Nano 33 BLE**

  - **IMU**: Built-in, connected internally.
  - **Potentiometer**:
    - **VCC**: Connect to 3.3V
    - **GND**: Connect to Ground
    - **Signal**: Connect to an analog input pin (e.g., A0)
  - **Flex Sensor**:
    - **One End**: Connect to 3.3V through a pull-up resistor (e.g., 10kΩ)
    - **Other End**: Connect to Ground
    - **Voltage Divider Point**: Connect to an analog input pin (e.g., A1)

#### Communication Interfaces

- **USB Connection**: The Arduino is connected to the computer via USB for serial communication.
- **Serial Communication**: Used to send sensor data from the Arduino to the control software on the computer.

### Power Supply

#### Requirements

- **Arduino Nano 33 BLE**: Powered via USB (5V from the computer).
- **Niryo One Robot**: Requires its own power supply (24V DC, provided with the robot).

#### Safety Considerations

- Ensure all devices are powered according to their specifications.
- Avoid short circuits by double-checking connections.
- Disconnect power before making changes to the wiring.

## Setup and Assembly

1. **Assemble the Sensors**

   - **Potentiometer**: Mount it securely where it can be easily adjusted.
   - **Flex Sensor**: Attach it to a glove or a flexible surface that bends with finger movement.
   - **IMU**: Since it's built into the Arduino Nano 33 BLE, secure the Arduino to the user's limb or a representative model.

2. **Connect the Sensors to the Arduino**

   - Wire the potentiometer and flex sensor to the appropriate analog input pins.
   - Use a breadboard and jumper wires as needed.

3. **Connect the Arduino to the Computer**

   - Use a USB cable to connect the Arduino to the computer running the control software.

4. **Set Up the Niryo One Robot**

   - Place the robot on a stable surface.
   - Connect the robot to its power supply.
   - Establish a connection between the robot and the computer (via Ethernet or Wi-Fi, as per the software setup).

5. **Install Necessary Software**

   - **Arduino IDE**: For programming the Arduino.
   - **Python and Niryo One Python API**: For controlling the robot from the computer.
   - **ROS (Robot Operating System)**: If required for advanced functionalities.

6. **Upload Arduino Code**

   - Write or use existing code to read sensor data and send it over serial communication.
   - Compile and upload the code to the Arduino using the Arduino IDE.

7. **Run Control Software**

   - On the computer, run the Python scripts that read data from the Arduino and send commands to the Niryo One robot.

## Troubleshooting

- **No Serial Communication**

  - Check USB connections.
  - Ensure the correct COM port is selected.
  - Verify baud rates match between the Arduino code and the Python script.

- **Sensor Readings Are Inaccurate**

  - Calibrate sensors if necessary.
  - Check for loose or faulty connections.
  - Replace sensors if defective.

- **Robot Not Responding**

  - Ensure the Niryo One is powered on.
  - Verify network connections between the robot and the computer.
  - Check for errors in the control software.

## Maintenance

- **Regularly Inspect Connections**

  - Ensure all wires and connections are secure.
  - Look for signs of wear or damage on sensors and cables.

- **Update Software**

  - Keep the Arduino firmware and control software up to date.
  - Update the Niryo One firmware as per the manufacturer's recommendations.

- **Clean Hardware**

  - Keep the robot and sensors free from dust and debris.
  - Use appropriate cleaning methods for electronic components.

## Future Improvements

- **Additional Sensors**

  - Integrate more advanced sensors like EMG (Electromyography) for muscle activity detection.

- **Wireless Communication**

  - Implement Bluetooth or Wi-Fi communication to eliminate USB cables.

- **Enhanced Control Algorithms**

  - Develop machine learning models for more intuitive control.

- **User Interface**

  - Create a graphical user interface (GUI) for easier interaction and monitoring.

## References

- **Niryo One's Software Application**

  - [Download Link](https://drive.google.com/drive/folders/1isq_ZBcwJi3rM7CoAoUcWk0g0jUqNlkB?usp=drive_link)

- **Lean Canvas**

  - [Lean Canvas Link](https://leanstack.com/ci/rlmastery/cohorts/foundations/canvases/827974)

- **Arduino Nano 33 BLE**

  - [Arduino Official Page](https://store.arduino.cc/arduino-nano-33-ble)

- **Sensor Datasheets**

  - **IMU (LSM9DS1)**: [Datasheet](https://www.st.com/resource/en/datasheet/lsm9ds1.pdf)
  - **Flex Sensor**: [Manufacturer Info](https://www.sparkfun.com/datasheets/Sensors/Flex/flex22.pdf)
  - **Potentiometer**: Refer to the specific model used.

---

By following this documentation, future developers should be able to understand and work with all the hardware components of the RoboLog project. If you have any questions or need additional assistance, feel free to reach out to the project maintainers.

---

*Note: Please ensure that all links are accessible and updated as per the project's resources.*
