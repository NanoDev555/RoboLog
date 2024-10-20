# -- coding: utf-8 --
import serial
import rospy
from niryo_one_python_api.niryo_one_api import NiryoOne, NiryoOneException
import time

rospy.init_node('niryo_one_control')

n = None
gripper_open = False  # For keeping track of gripper state
robot_speed = 25  # Lower speed for smoother movements
potentiometer_threshold = 50  # Threshold for potentiometer (Joint 3)
imu_threshold = 0.05  # Threshold for IMU (Joint 1 and 2)
gripper_button_pin = 2  # Arduino digital pin for the gripper button
scaling_factor = 2.0  # Scaling factor for IMU to amplify movement

def connect_to_robot():
    global n
    while n is None:
        try:
            n = NiryoOne()
            print("Connection to Niryo One succeeded!")
        except NiryoOneException as e:
            print("Failed to connect to the robot: {}".format(str(e)))
            time.sleep(5)

def select_tool():
    try:
        print("Selecting Gripper 1 (ID 11)...")
        n.change_tool(11)  # Select Gripper 1
        print("Gripper 1 is selected!")
    except NiryoOneException as e:
        print("Failed to select Gripper 1: {}".format(str(e)))

connect_to_robot()
time.sleep(5)  # Wait for the action server to start
select_tool()

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
ser.flush()

JOINT_1_MIN = -3.0
JOINT_1_MAX = 3.0
JOINT_2_MIN = -1.92
JOINT_2_MAX = 0.64
JOINT_3_MIN = -1.57
JOINT_3_MAX = 1.57

def map_value_to_radians(value, from_low, from_high, to_low, to_high):
    return to_low + (float(value - from_low) / float(from_high - from_low)) * (to_high - to_low)

def clamp_value(value, min_value, max_value):
    return max(min_value, min(max_value, value))

def toggle_gripper(open_gripper):
    global gripper_open
    try:
        if open_gripper:
            n.open_gripper(11, 500)   # Open gripper at speed 500
            print("Gripper is opening")
            gripper_open = True
        else:
            n.close_gripper(11, 500)  # Close gripper at speed 500
            print("Gripper is closing")
            gripper_open = False
    except NiryoOneException as e:
        print("Niryo One Exception: {}".format(str(e)))

def move_joints_to_final_position(x_accel, y_accel, pot_value3):
    n.set_arm_max_velocity(robot_speed)  # Set the robot's max velocity for smoother movements
    joint1_value = clamp_value(y_accel * scaling_factor, JOINT_1_MIN, JOINT_1_MAX) if abs(y_accel) >= imu_threshold else 0
    joint2_value = clamp_value(x_accel * scaling_factor, JOINT_2_MIN, JOINT_2_MAX) if abs(x_accel) >= imu_threshold else 0
    joint3_value = map_value_to_radians(pot_value3, 0, 1023, JOINT_3_MIN, JOINT_3_MAX) if abs(pot_value3 - lastPotValue3) >= potentiometer_threshold else map_value_to_radians(lastPotValue3, 0, 1023, JOINT_3_MIN, JOINT_3_MAX)
    try:
        n.move_joints([joint1_value, joint2_value, joint3_value, 0, 0, 0])
        print("Robot is moving to final position: Joint 1 = {}, Joint 2 = {}, Joint 3 = {}".format(joint1_value, joint2_value, joint3_value))
    except NiryoOneException as e:
        print("Niryo One Exception: {}".format(str(e)))

lastPotValue3 = 0  # Save last potentiometer value
try:
    while not rospy.is_shutdown():
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            y_accel, x_accel, pot_value3, button_state = map(float, data.split(','))  # Adjust to match your serial output format
            
            # Control the gripper based on button state
            if button_state == 1 and not gripper_open:
                toggle_gripper(True)  # Open the gripper
            elif button_state == 0 and gripper_open:
                toggle_gripper(False)  # Close the gripper

            if (abs(y_accel) >= imu_threshold or abs(x_accel) >= imu_threshold or 
                abs(pot_value3 - lastPotValue3) >= potentiometer_threshold):
                move_joints_to_final_position(x_accel, y_accel, pot_value3)

            lastPotValue3 = pot_value3  # Update the potentiometer value

except NiryoOneException as e:
    print("Niryo One Exception: {}".format(str(e)))
