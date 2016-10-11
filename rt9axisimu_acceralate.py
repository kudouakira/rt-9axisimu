#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

def callback(message):
    ac.x = message.imu.x
    ac.y = message.imu.y
    ac.z = message.imu.z

if __name__ == '__main__':
    rospy.init_node('acceralate')
    sub = rospy.Subscriber('/imu/data_raw', Imu, callback)

    r = rospy.Rate(0.5)
    print "===rt-9axisimu-acceralate===\n\n\n"
    while not rospy.is_shutdown():
        print "--------------------"
        print ac.x
        print ac.y
        print ac.z
        print "--------------------"
        r.sleep()

