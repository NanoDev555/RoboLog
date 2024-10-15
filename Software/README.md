# RoboLog Software Documentation

## Introduction

This document provides detailed information about the software components of the RoboLog project. It is intended for future developers who will take over the project next year, helping them understand the software architecture, codebase, and how it interfaces with the hardware components.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Software Architecture](#software-architecture)
   - [System Components](#system-components)
   - [Data Flow](#data-flow)
3. [Setup and Installation](#setup-and-installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [Code Structure](#code-structure)
   - [Arduino Code](#arduino-code)
   - [Python Scripts](#python-scripts)
5. [Interfacing with Hardware](#interfacing-with-hardware)
   - [Sensor Integration](#sensor-integration)
   - [Communication Protocols](#communication-protocols)
6. [Running the Software](#running-the-software)
   - [Arduino Firmware](#arduino-firmware)
   - [Python Control Scripts](#python-control-scripts)
7. [Testing and Calibration](#testing-and-calibration)
   - [Sensor Calibration](#sensor-calibration)
   - [Robot Movement Testing](#robot-movement-testing)
8. [Troubleshooting](#troubleshooting)
9. [Future Improvements](#future-improvements)
10. [Contributing](#contributing)
11. [License](#license)
12. [References](#references)

## Project Overview

The RoboLog project aims to develop a prosthetic arm controlled through sensor inputs to mimic natural human movements. The software components are responsible for reading sensor data, processing inputs, and commanding the Niryo One robotic arm accordingly.

## Software Architecture

### System Components

- **Arduino Nano 33 BLE**: Collects data from built-in and external sensors.
- **Python Scripts**: Run on a computer to process sensor data and control the Niryo One robot.
- **Niryo One Python API**: Library used to send commands to the robot.

### Data Flow

1. **Sensor Data Acquisition**: Arduino reads data from the IMU, potentiometer, and flex sensor.
2. **Data Transmission**: Sensor data is sent from the Arduino to the computer via serial communication.
3. **Data Processing**: Python scripts read and process the sensor data.
4. **Robot Control**: Processed data is used to generate movement commands for the Niryo One robot.

## Setup and Installation

### Prerequisites

- **Hardware**:
  - Arduino Nano 33 BLE
  - Niryo One Robot
- **Software**:
  - Arduino IDE
  - Python 3.x
  - Niryo One Python API
  - Ubuntu 20.04 (recommended)
- **Libraries**:
  - `Arduino_LSM9DS1` for IMU
  - `pySerial` for serial communication

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/robolog.git

