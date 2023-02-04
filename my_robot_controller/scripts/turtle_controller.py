#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist     #msg for topics
from turtlesim.srv import SetPen    #srv for services

previous_x = 0
#definir a funcao para chamar o servico
def call_set_pen_service(r,g,b,width,off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r,g,b,width,off)
        #rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.logwarn(e)


# publisher and subscriber

#publisher callback
def pose_callback(msg: Pose):
    cmd =  Twist()
    if msg.x > 9.0 or msg.x <2.0 or msg.y>9.0 or msg.y <2.0:       # if the turtle is in the right side of the screen
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    pub.publish(cmd)
    

#service client
    global previous_x
    if msg.x >= 5.5 and previous_x < 5.5:
        rospy.loginfo("Set color to red")
        call_set_pen_service(255,0,0,3,0)
    elif msg.x < 5.5 and previous_x >= 5.5:
        call_set_pen_service(0,255,0,3,0)
        rospy.loginfo("Set color to green")
    previous_x = msg.x

if __name__ =="__main__":
    
    rospy.init_node("turtle_controller")
    rospy.wait_for_service("/turtle1/set_pen")    
    # call_set_pen_service(255,0,0,3,0)
    pub = rospy.Publisher ("/turtle1/cmd_vel", Twist ,queue_size=10 )
    sub = rospy.Subscriber("/turtle1/pose", Pose , callback=pose_callback )
    
    rospy.loginfo("Node has been started")

    rospy.spin()

