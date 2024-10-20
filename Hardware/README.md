# RoboLog Hardware Documentation

## Introduction

This document provides detailed information about the hardware components used in the RoboLog project. It is intended for future developers who will take over the project next year, helping them understand the role and integration of each hardware part.

## Table of Contents

1. [Overview](#overview)
2. [Hardware Components](#hardware-components)
   - [Niryo One Robot](#niryo-one-robot)
   - [Arduino Nano 33 BLE](#arduino-nano-33-ble)
   - [Potentiometer](#potentiometer)
   - [Sensor](#sensor)
     - [Flex Sensor](#flex-sensor)
   - [Connections and Wiring](#connections-and-wiring)
   - [Power Supply](#power-supply)
3. [Maintenance](#maintenance)
4. [Images](#Images)
5. [Future Improvements](#future-improvements)
6. [References](#references)

## Overview

The RoboLog project aims to develop a prosthetic arm controlled through various sensor inputs to mimic natural human movements. The hardware setup includes a Niryo One robotic arm, an Arduino Nano 33 BLE microcontroller (which has a built-in IMU), and several external sensors that capture user input.

## Hardware Components

### Niryo One Robot

#### Description

The **Niryo One** is a 6-axis collaborative robotic arm. It is powered by ROS (Robot Operating System) and allows for advanced programming and control.

#### Specifications

- **Degrees of Freedom**: 6
- **Payload**: Up to 0.5 kg
- **Reach**: 440 mm
- **Weight**: 3kg
- **Repeatabillity**: 3kg
- **Software Compatibility**: ROS, Python APIs
- **End Effectors**: Gripper, vacuum pump, electromagnet (the gripper is used in this project)

#### Role in the Project

The Niryo One serves as the physical prosthetic arm, executing movements based on sensor input. It mimics the natural motion of a human arm by responding to real-time data from the sensors.

### Arduino Nano 33 BLE

#### Description

The **Arduino Nano 33 BLE** is a compact microcontroller board featuring Bluetooth Low Energy connectivity and an onboard IMU (Inertial Measurement Unit).

#### Features

- **Microcontroller**: nRF52840 (ARM Cortex-M4 CPU)
- **Operating Voltage**: 3.3V
- **Digital I/O Pins**: 14
- **Analog Input Pins**: 8
- **Connectivity**: Bluetooth 5.0 BLE
- **Built-in Sensor**: 9-axis IMU (LSM9DS1)

#### Role in the Project

The Arduino Nano 33 BLE collects data from its built-in IMU and connected external sensors (potentiometer and flex sensor), sending this data to the control software running on a computer, which then commands the Niryo One robot.


#### Potentiometer

##### Description

A potentiometer is a three-terminal resistor with a sliding contact that forms an adjustable voltage divider.

##### How It's Used

- **Manual Control**: Allows the user to adjust the position of a specific joint on the robot manually.
- **Data Output**: Provides variable resistance translated into position values for the robot's joint.

### Sensor

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

  - **Built-in IMU**: No wiring required; accessible via code.
  - **Potentiometer**:
    - **VCC**: Connect to 3.3V
    - **GND**: Connect to Ground
    - **Signal**: Connect to an analog input pin (e.g., A0)
  - **Flex Sensor**:
    - **One End**: Connect to 3.3V through a pull-up resistor (e.g., 10kΩ)
    - **Other End**: Connect to GND


## Power Supply

### Requirements

- **Arduino Nano 33 BLE**: Powered via USB (5V from the computer).
- **Niryo One Robot**: Requires its own power supply (24V DC, provided with the robot).

### Safety Considerations

- Ensure all devices are powered according to their specifications.
- Avoid short circuits by double-checking connections.
- Disconnect power before making changes to the wiring.

## Maintenance

- **Regularly Inspect Connections**

  - Ensure all wires and connections are secure.
  - Look for signs of wear or damage on sensors and cables.

- **Update Software**

  - Keep the Arduino firmware and control software up to date.
  - Update the Niryo One firmware as per the manufacturer's recommendations.
 
## Images
![WhatsApp Image 2024-10-20 at 19 15 29_97d9d472](https://github.com/user-attachments/assets/54e9ae37-9c08-4281-9ff6-bf2c928101f2){: width="800px" }

 
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

  - **Flex Sensor**: [Manufacturer Info](https://www.sparkfun.com/datasheets/Sensors/Flex/flex22.pdf)
  - **Potentiometer**: Provided by KTH.


