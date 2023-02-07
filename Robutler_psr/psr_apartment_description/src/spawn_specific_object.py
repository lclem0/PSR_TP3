#!/usr/bin/env python3

import random
import yaml
import rospy
import rospkg
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose, Point, Quaternion

rospy.init_node('insert_object',log_level=rospy.INFO)

# get an instance of RosPack with the default search paths
rospack = rospkg.RosPack()
package_path = rospack.get_path('psr_apartment_description') + '/description/models/'

with open("/home/lclem0/catkin_ws/src/PSR_TP3/Robutler_psr/psr_apartment_description/src/apartment_spots.yaml", 'r') as file:
        pose = yaml.load(file, Loader=yaml.FullLoader)
    
        divisions = []
        places = []
        poses = []
        for i in range(0, len(pose)):
            division = pose[i]["room"]
            # if division not in divisions:
            place = pose[i]["place"]
            places.append(place)
            positions = pose[i]["pose"]
            poses.append(positions)
            divisions.append(place + " in " + division)
        # places_list = list(set(places))
        divisions_list = list(set(divisions))

model_names = ['sphere_v','stop_sign','person_standing','beer','person_walking','fire_hydrant']

object_str = input("From the objects list: " + str(model_names) + ", select the index of the one you would like to spawn: ")
object_id= int(object_str)
if object_id > len(model_names)-1:
    rospy.logerr("Please enter a number between 0 and " + str(len(model_names)-1))
    exit()
else:
    selected_object = model_names[object_id]
    rospy.loginfo('You selected the object: ' + selected_object)

room_str = input("From the rooms list: " + str(divisions) + ",Select the index of the one you would like to spawn the object in: ")
room_id = int(room_str)
if room_id > len(divisions_list)-1:
    rospy.logerr('Please enter a number between 0 and ' + str(len(divisions)-1))
    exit()
else:
    selected_room = divisions[room_id]
    rospy.loginfo('You selected the room: ' + selected_room)

placements = []
placements.append({'pose':Pose(position=Point(x=-5.69, y=4.37, z=0.6), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'first_bedroom', 'place': 'bed'})
placements.append({'pose':Pose(position=Point(x=-7.33, y=5.29, z=0.58), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'first_bedroom', 'place': 'bedside_cabinet'})
            #   adicionar mais sitios
placements.append({'pose':Pose(position=Point(x=-1.7, y=4.0, z=0.37), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'second_bedroom', 'place': 'fridge_cabinet'})
placements.append({'pose':Pose(position=Point(x=-2, y=-4, z=0.0), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'living_room', 'place': 'ground'})
placements.append({'pose':Pose(position=Point(x=1, y=-3, z=0), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'outside', 'place': 'car_spot'})
placements.append({'pose':Pose(position=Point(x=-6, y=-2, z=0.765), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'living_room', 'place': 'coffee_table'})
placements.append({'pose':Pose(position=Point(x=1.74, y=-0.7, z=0.5), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'bathroom_toilet', 'place': 'toilet'})
placements.append({'pose':Pose(position=Point(x=-2.5, y=5, z=0), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'second_bedroom', 'place': 'ground'})
placements.append({'pose':Pose(position=Point(x=0, y=5, z=0), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'office', 'place': 'ground'})
placements.append({'pose':Pose(position=Point(x=0.5, y=1.5, z=0), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'empty_bathroom', 'place': 'ground'})
placements.append({'pose':Pose(position=Point(x=-3, y=1.5, z=0), orientation=Quaternion(x=0,y=0,z=1,w=1)),
'room':'corridor', 'place': 'ground'})
placements.append({'pose':Pose(position=Point(x=-7.5, y=-0.5, z=0), orientation=Quaternion(x=0,y=0,z=0,w=1)),
'room':'ouside_corridor', 'place': 'ground'})
placements.append({'pose':Pose(position=Point(x=-1.7, y=-0.5, z=0.8), orientation=Quaternion(x=0,y=0,z=0,w=1)),
'room':'kitchen', 'place': 'counter'})
# placements.append({'pose':Pose(position=Point(x=-4.5, y=-2, z=0), orientation=Quaternion(x=0,y=0,z=1,w=1)),
# 'room':'empty_bathroom', 'place': 'ground'})
placements.append({'pose':Pose(position=Point(x=-1, y=-5, z=0), orientation=Quaternion(x=0,y=0,z=0,w=1)),
'room':'living_room', 'place': 'corner'})

#save the model
f = open( package_path + selected_object + '/model.sdf' ,'r')
sdff = f.read()

rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)


name = selected_object + '_in_' + places[room_id] + '_of_' + selected_room
print(name)
spawn_model_prox(name, sdff, selected_object, placements[room_id]["pose"], "world")
rospy.loginfo(name)
i+=1



