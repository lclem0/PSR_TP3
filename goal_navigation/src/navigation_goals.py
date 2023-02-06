#!/usr/bin/env python3

import sys
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,  MoveBaseGoal
sys.path.append('/opt/ros/noetic/lib/python3/dist-packages')


def active_cb(extra):
    rospy.loginfo("Goal pose is now being processed by the Action Server...")

def feedback_cb(feedback):
    rospy.loginfo("Feedback for goal pose: " + str(feedback))

def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal pose reached!")
    else:
        rospy.loginfo("The base failed to reach the goal for some reason")


rospy.init_node('send_goal')
#create a client to send goal requests to the move_base server through a SimpleActionClient
navclient = actionlib.SimpleActionClient('move_base', MoveBaseAction)
navclient.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.pose.position.x = -5.5
goal.target_pose.pose.position.y = -1.0
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
goal.target_pose.pose.orientation.z = 0.0
goal.target_pose.pose.orientation.w = 1.0

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finished=navclient.wait_for_result()

if not finished:
    rospy.logerr("Action server not available!")
    rospy.signal_shutdown("Action server not available!")
else:
    rospy.loginfo("Action finished!")






