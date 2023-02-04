#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

#publisher

if __name__ == '__main__':
    rospy.init_node('draw_circle')   #node, inside the executable

    rospy.loginfo("Node has been started")

    pub = rospy.Publisher("/turtle1/cmd_vel" , Twist, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        #publish command velocity
        msg = Twist()   #create a message-object from the class Twist
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        pub.publish(msg)
        rate.sleep()