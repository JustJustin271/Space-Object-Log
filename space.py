# Created on June 8th, 2026
# Last edited on June 10th, 2026
# Justin C.

# Takes in the number of times to loop
object_count = int(input())

# Keeps track of information in dictionary
object_dict = {
    "meteoroid": 0,
    "asteroid": 0,
    "planetoid": 0
}

# Records all of closest and biggest information
closest_dist = 0
biggest_size = 0

closest_name = ""
biggest_name = ""


# Loops for the amount of objects that were given
for object in range(object_count):
   
    # Splits it into a readily usable list
    object_info = input().split()
   
    # Extracts list information into variables
    name = object_info[0]
    distance = abs(int(object_info[1])) + abs(int(object_info[2]))
    diameter = int(object_info[3])
   
   
    # Checks for what is it by judging it by size
    if diameter < 50:
        object_dict["meteoroid"] = object_dict["meteoroid"] + 1
    elif diameter < 500:
        object_dict["asteroid"] = object_dict["asteroid"] + 1
    else:
        object_dict["planetoid"] = object_dict["planetoid"] + 1
   
    # Records/Updates and checks for closest and smallest
    if object == 0:
        closest_dist = distance
        biggest_size = diameter
       
        closest_name = name
        biggest_name = name
       
    if distance < closest_dist:
        closest_name = name
        closest_dist = distance
   
    if diameter > biggest_size:
        biggest_size = diameter
        biggest_name = name

#Prints out all of the information needed
print(f"meteoroid: {object_dict["meteoroid"]}")
print(f"asteroid: {object_dict["asteroid"]}")
print(f"planetoid: {object_dict["planetoid"]}")
print(f"Closest: {closest_name}")
print(f"Biggest: {biggest_name}")
