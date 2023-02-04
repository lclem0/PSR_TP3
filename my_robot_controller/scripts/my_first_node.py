#!/usr/bin/env python3

import rospy


if __name__ == '__main__':
    rospy.init_node('test_node')   #node, inside the executable

    rospy.loginfo('Hello from test node!')
    rospy.logwarn("This is a warning")
    rospy.logerr("This is an error")
    rospy.logdebug("This is a debug message")

    rospy.sleep(1.0) 
    rospy.loginfo("End of the program")         #work as a print 



    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("hello")
        rate.sleep()