#!/usr/bin/env python
import rosh
import time
import rospy

rosh.rosh_init()

power = 8.15
steer2 = 1.73
steer1 = 1.26


power_cmd = rosh.msg.std_msgs.Float64()
steer_cmd_1 = rosh.msg.std_msgs.Float64()
steer_cmd_2 = rosh.msg.std_msgs.Float64()

power_cmd.data = power
steer_cmd_1.data = steer1
steer_cmd_2.data = steer2

left_steer = getattr(rosh.topics, '/robot_gazebo/left_wheel_steering_controller/command')
left_power = getattr(rosh.topics, '/robot_gazebo/left_wheel_power_controller/command')
right_steer = getattr(rosh.topics, '/robot_gazebo/right_wheel_steering_controller/command')
right_power = getattr(rosh.topics, '/robot_gazebo/right_wheel_power_controller/command')


while True:

    left_steer(steer_cmd_1)
    right_steer(steer_cmd_2)
    left_power(power_cmd)
    right_power(power_cmd)
    time.sleep(0.5)
