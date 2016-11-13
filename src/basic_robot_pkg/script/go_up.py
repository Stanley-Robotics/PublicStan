#!/usr/bin/env python
import rosh
import time
import rospy

rosh.rosh_init()

power = 0
steer = 0.0
extend = 0.0


power_cmd = rosh.msg.std_msgs.Float64()
steer_cmd = rosh.msg.std_msgs.Float64()
extend_cmd = rosh.msg.std_msgs.Float64()

power_cmd.data = power
steer_cmd.data = steer
extend_cmd.data = extend

left_steer = getattr(rosh.topics, '/robot_gazebo/left_wheel_steering_controller/command')
left_power = getattr(rosh.topics, '/robot_gazebo/left_wheel_power_controller/command')
right_steer = getattr(rosh.topics, '/robot_gazebo/right_wheel_steering_controller/command')
right_power = getattr(rosh.topics, '/robot_gazebo/right_wheel_power_controller/command')

extend = getattr(rosh.topics, '/robot_gazebo/central_cylinder_controller/command')

pillow_front = getattr(rosh.topics, '/robot_gazebo/pillow_front_controller/command')
pillow_back = getattr(rosh.topics, '/robot_gazebo/pillow_back_controller/command')

while True:

    left_steer(steer_cmd)
    right_steer(steer_cmd)
    left_power(power_cmd)
    right_power(power_cmd)
    extend(extend_cmd)
    pillow_front(0.1)
    pillow_back(0.1)
    time.sleep(0.01)

