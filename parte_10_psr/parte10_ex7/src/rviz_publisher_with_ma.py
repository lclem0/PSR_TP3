#!/usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

def main():
    
    rospy.init_node("rviz_publisher", anonymous=False)
    pub = rospy.Publisher("~markers",MarkerArray, queue_size=1)
    rate = rospy.Rate(1)


    while not rospy.is_shutdown():
        
        #create a marker
        marker_array = MarkerArray()


        #criar marcador para esfera
        marker = Marker()        
        marker.header.frame_id = "world"    #arbitrario
        # marker.header.stamp = rospy.Time.now()
        marker.ns = "my_drawings"
        marker.id = 0   #id do marker
        marker.type = marker.SPHERE
        marker.action = marker.MODIFY
        
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.0

        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 1.0
        marker.pose.orientation.w = 0.0
        
        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 3
        
        marker.color.a = 0.3    #transparencia nao pode ser 0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
   
        marker.text = "Not used"

        marker_array.markers.append(marker)     #add marker to marker array
        #publish the marker
        pub.publish(marker)
        rate.sleep()



if __name__ == "__main__":
    main()

