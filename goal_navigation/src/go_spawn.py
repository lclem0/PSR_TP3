#!/usr/bin/env python3

import rospy
import actionlib
import tf
from geometry_msgs import *
from geometry_msgs.msg import PoseStamped


rospy.init_node('go_spawn',anonymous=True)
pub = rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=1)

spawn_pose = PoseStamped()
spawn_pose.header.frame_id = "map"
spawn_pose.pose.position.x = -5.5
spawn_pose.pose.position.y = -1.0
spawn_pose.pose.position.z = 0.0
spawn_pose.pose.orientation.x = 0.0
spawn_pose.pose.orientation.y = 0.0
spawn_pose.pose.orientation.z = 0.0
spawn_pose.pose.orientation.w = 1.0

rospy.sleep(1)
rospy.loginfo("Going to spawn")
pub.publish(spawn_pose)
rospy.loginfo("At spawn")

