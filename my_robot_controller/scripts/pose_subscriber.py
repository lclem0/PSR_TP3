#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

#subscriber

def pose_callback(msg:Pose):
    rospy.loginfo( "(" + str(msg.x) + "," + str(msg.y) + ")" )

if __name__=='__main__':

    rospy.init_node("turtle_pose_subscriber")
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)     #primeiro o nome do topico, depois o tipo de mensagem, 
    #depois a funcao que vai ser chamada quando a mensagem chegar

    rospy.loginfo("Node has been started")
    rospy.spin()