#!/usr/bin/env python3
import rospy
import tf
from interactive_markers.interactive_marker_server import *
from visualization_msgs.msg import *
from geometry_msgs.msg import PoseStamped, Pose

def processFeedback(feedback):
    # Get the current pose of the end-effector link
    try:
        (trans, rot) = listener.lookupTransform('base_link', 'end_effector_link', rospy.Time(0))
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        return

    # Update the end-effector link's pose based on the interactive marker's feedback
    new_pose = Pose()
    new_pose.position.x = trans[0] + feedback.pose.position.x
    new_pose.position.y = trans[1] + feedback.pose.position.y
    new_pose.position.z = trans[2] + feedback.pose.position.z
    new_pose.orientation = feedback.pose.orientation
    end_effector_pose_stamped = PoseStamped()
    end_effector_pose_stamped.header.frame_id = 'base_link'
    end_effector_pose_stamped.pose = new_pose

    # Publish the new end-effector pose
    end_effector_pose_publisher.publish(end_effector_pose_stamped)

if __name__=="__main__":
    rospy.init_node("interactive_marker")
    
    # Create a TF listener
    listener = tf.TransformListener()

    # Create a publisher for the end-effector link's pose
    end_effector_pose_publisher = rospy.Publisher('end_effector_pose', PoseStamped, queue_size=10)

    # Create an interactive marker server
    server = InteractiveMarkerServer("interactive_marker")

    # Create an interactive marker for the end-effector link
    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "base_link"
    int_marker.name = "end_effector_marker"
    int_marker.description = "End-Effector Control"

    # Create a sphere marker for the interactive marker
    sphere_marker = Marker()
    sphere_marker.type = Marker.SPHERE
    sphere_marker.scale.x = 0.1
    sphere_marker.scale.y = 0.1
    sphere_marker.scale.z = 0.1
    sphere_marker.color.r = 1.0
    sphere_marker.color.g = 0.0
    sphere_marker.color.b = 0.0
    sphere_marker.color.a = 1.0

    # Create a control for the interactive marker
    sphere_control = InteractiveMarkerControl()
    sphere_control.always_visible = True
    sphere_control.markers.append(sphere_marker)
    int_marker.controls.append(sphere_control)



