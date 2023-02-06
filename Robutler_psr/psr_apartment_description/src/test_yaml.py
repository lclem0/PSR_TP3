import yaml

with open("/home/lclem0/catkin_ws/src/PSR_TP3/Robutler_psr/psr_apartment_description/src/apartment_spots.yaml", 'r') as file:
    pose = yaml.load(file, Loader=yaml.FullLoader)
    
    divisions = []
    for i in range(0, len(pose)):
        division = pose[i]["room"]
        divisions.append(division)
    divisions_list = list(set(divisions))
    # print(divisions_list)
    # print(len(divisions_list))