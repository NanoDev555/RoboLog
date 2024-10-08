# RoboLog

## Introduktion
-------------------
RoboLog is a project focused on creating a prosthetic arm controlled by sensor inputs like a potentiometer, IMU (Inertial Measurement Unit), and a flex sensor. The project integrates sensor data to precisely control the movements of a prosthetic arm's joints and its gripping function. This solution is designed to provide users with smooth and responsive control over the arm, mimicking natural movements.

This project is particularly useful for developers and researchers working on prosthetic technology, assistive devices, and rehabilitation systems that require precise and adaptive control mechanisms for human limb replacements.

## Prerequisites
------------------
Before running the RoboLog project, you need the following:

- Niryo One Robot and its software (The link for the software file is down below)

- Arduino Nano 33 BLE board: Used for reading sensor inputs like the in-build IMU, flex sensor and potentiometer.

- Arduino IDE: For compiling and uploading the Arduino code.

- Ubuntu 20.04: Ubuntu is an essential platform for developing and running the RoboLog prosthetic arm project, providing a stable environment for Python scripting and Arduino integration. Its wide range of development tools and open-source support makes it ideal for controlling sensor-driven systems like prosthetic devices. 

- Niryo One Python API: A library to communicate with and control the Niryo One robot.

- IMU (Accelerometer): Built-in on the Arduino Nano 33 BLE for detecting joint movements. IMU takes 3D movement(x, y och z)

- Potentiometer: For manual control of one of the robot's joints.

- Flex Sensor: For controlling the gripper.

- USB cables: To connect Arduino to the computer running the Python code.

- Serial communication: Between Arduino and Python for real-time control.

## Installations
------------------
1. Download the Niryo One software application from the link down below.
2. Download and install the Arduino IDE from [Arduino's official website](https://www.arduino.cc/en/software).
3. Install the necessary libraries, such as the Arduino_LSM9DS1 library for the IMU, through the Arduino IDE Library Manager.
4. Download the Ubuntu 20.04 from the Microsoft store.
5. Install packages in Ubuntu by following the steps here [ROSInstallation](ROSInstallation)


## Getting the Niryo One started
--------------------------------------
After installing all the necessary programs and packages, you need to connect the laptop to the robot. There are two ways to do this, and here are the step-by-step instructions for each method:

- Method one:

Use the hotspot in the Niryo One software app and connect to it using Wi-Fi. Note that by using this method, your laptop will lose internet connection.

- Method two (recommended):

Use an Ethernet cable. In this case, you need to select the IP address you want to connect to in the Niryo One software app. The IP address you need to use is "169.254.200.200". By using this method, you will still have an internet connection on your laptop.

Now, after you are connected to the robot, you have to start the Ubuntu 20.4 application. There are some commands you need to use to run or save codes on the Rasberry PI board.

First of all, start Ubuntu and then type in these commands to access the files in the Rasberry PI board and edit or add codes to it:
1.  To connect to the robot type in this command:

***ssh niryo@169.254.200.200***

2. Ubunto will ask you to type in a password to access the robot, the password is: ***robotics***
3. Type in the command ***source ~/.bashrc*** to be able then to add, edit and run your codes.
4. By typing the command ***"nano"*** then ***"ctrl + R"*** and then ***"ctrl + T"***, you will access the files and there you will be able to add your Python codes.
5. By typing the command ***"nano YOUR.FILE.NAME.PY"*** You will go to the requested file without going to the files menu.
6. To run a code you use the command ***python YOUR.FILE.NAME.PY***.

- After you run the code, you will be able to control the robot according to your code. 


## Bidra
Information om hur andra kan bidra till projektet.

## Licens
Information om licensen för projektet.



-  Niryo Ones software application:
https://drive.google.com/drive/folders/1isq_ZBcwJi3rM7CoAoUcWk0g0jUqNlkB?usp=drive_link

- Lean Canvas
https://leanstack.com/ci/rlmastery/cohorts/foundations/canvases/827974
