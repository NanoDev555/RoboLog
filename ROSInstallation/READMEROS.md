# Introduction

This guide walks you through the installation of ROS Noetic on Ubuntu for the RoboLog project. ROS Noetic provides the necessary tools for robotic control and is compatible with Ubuntu 20.04. We recommend following the steps below to install the full ROS Desktop environment, but you can choose other options based on your needs.

- Before installing ROS, you need to enable certain Ubuntu repositories:

Open a terminal and configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse."


sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository restricted


## Step-by-Step Installation

1. Add the ROS Noetic package sources:
Configure your system to accept software from the ROS package repository:

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

2. Set up the ROS keys:
Install curl if it's not already installed, and then add the ROS key:

sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -


3. Update package list:
Update your local package index:

sudo apt update

4. Install ROS Noetic:
There are multiple versions of ROS you can install, based on what you need:

- Desktop-Full Install (recommended): This includes everything, including simulators and perception packages.

sudo apt install ros-noetic-desktop-full

- Desktop Install: Includes core ROS packages and visualization tools like rviz.

sudo apt install ros-noetic-desktop

- ROS-Base (Bare Bones): Includes only the core ROS packages, with no GUI tools.

sudo apt install ros-noetic-ros-base

- To find specific ROS packages:

apt search ros-noetic

5. Set up your environment:
You need to source the ROS environment setup script in every terminal where you plan to use ROS. Add the following to your .bashrc to automatically source ROS each time you open a new terminal:


echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

- For zsh users, replace the above with:

echo "source /opt/ros/noetic/setup.zsh" >> ~/.zshrc
source ~/.zshrc

6. Install dependencies for building packages:
If you plan to create your own ROS packages, install these additional dependencies:


sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

- Initialize rosdep:

sudo rosdep init
rosdep update

- After you follow the steps above, you will have accsess to the Niryo One Rasberry pi board and then you can add your python files and run it to control the robot.

