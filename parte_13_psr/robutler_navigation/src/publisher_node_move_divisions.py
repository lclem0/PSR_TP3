#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def move_to_goal():
    rospy.init_node('publisher_node', anonymous=True)
    pub = rospy.Publisher('/move_base/goal', PoseStamped, queue_size=10)
    rate = rospy.Rate(10)  # 10hz
    
    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = -4.0
    goal.pose.position.y = 2.0
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0

    while not rospy.is_shutdown():
        pub.publish(goal)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_to_goal()
    except rospy.ROSInterruptException:
        pass




