# RoboLog

## Introduktion
RoboLog is a project focused on creating a prosthetic arm controlled by sensor inputs like a potentiometer, IMU (Inertial Measurement Unit), and a flex sensor. The project integrates sensor data to precisely control the movements of a prosthetic arm's joints and its gripping function. This solution is designed to provide users with smooth and responsive control over the arm, mimicking natural movements.

This project is particularly useful for developers and researchers working on prosthetic technology, assistive devices, and rehabilitation systems that require precise and adaptive control mechanisms for human limb replacements.

## Prerequisites
Before running the RoboLog project, you need the following:

- Niryo One Robot and its software (The link for the software file is down below)

- Arduino Nano 33 BLE board: Used for reading sensor inputs like the in-build IMU, flex sensor and a potentiometer.

- Arduino IDE: For compiling and uploading the Arduino code.

- Ubuntu 20.04 : Ubuntu is a essential platform for developing and running the RoboLog prosthetic arm project, providing a stable environment for Python scripting and Arduino integration. Its wide range of development tools and open-source support makes it ideal for controlling sensor-driven systems like prosthetic devices. 

- Niryo One Python API: A library to communicate with and control the Niryo One robot.

- IMU (Accelerometer): Built-in on the Arduino Nano 33 BLE for detecting joint movements. IMU takes 3D movement(x, y och z)

- Potentiometer: For manual control of one of the robot's joints.

- Flex Sensor: For controlling the gripper.

- USB cables: To connect Arduino to the computer running the Python code.

- Serial communication: Between Arduino and Python for real-time control.

- 
## Installation
1. Download and install the Arduino IDE from Arduino's official website.
2. Install the necessary libraries, such as the Arduino_LSM9DS1 library for the IMU, through the Arduino IDE Library Manager.
3. Connect your Arduino Nano 33 BLE Sense to your computer via USB.
4- Download and install the Ubuntu 20.04 official website.
5- Install packages in Ubuntu by following the steps here [Link Text](ROSInstallation)


## Användning
Instruktioner om hur man använder projektet efter installation.

## Bidra
Information om hur andra kan bidra till projektet.

## Licens
Information om licensen för projektet.



Mjukvaran för Niryo One robot arm
https://drive.google.com/drive/folders/1isq_ZBcwJi3rM7CoAoUcWk0g0jUqNlkB?usp=drive_link

Lean Canvas
https://leanstack.com/ci/rlmastery/cohorts/foundations/canvases/827974
