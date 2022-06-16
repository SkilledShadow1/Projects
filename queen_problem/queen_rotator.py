import json
from copy import deepcopy

#MAKE SURE BOARD SIZES ARE THE SAME IMPORTANT
board_size = 9

with open ('queen_placement.json', 'r') as f:
    info = json.load(f)

num_letter_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 
                         'f': 6, 'g': 7, 'h': 8, 'i':9, 'j': 10, 'k': 11, 'm': 12}    

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

number_list = number_list[:board_size]

def sort_queens(queen_coordinates):
    sorted_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm']
    sorted_list = sorted_list[:board_size]
    s_list_copy = deepcopy(sorted_list)
    for coordinate in queen_coordinates:
        for letter in sorted_list:
            if coordinate[0] == letter:
                s_list_copy[s_list_copy.index(letter)] = coordinate
                
    return s_list_copy


def num_letter_switch(unit):
    if type(unit) == int:
        for key, value in num_letter_dictionary.items():
            if value == unit:
                new_unit = key
        
    if type(unit) == str:
        for key, value in num_letter_dictionary.items():
            if key == unit:
                new_unit = value
            
    return new_unit

def find_opposite(unit):
    if type(unit) == int:
        new_unit = number_list[-1 * unit]
    
    if type(unit) == str:
        new_unit = number_list[num_letter_switch(unit) * -1]
        new_unit = num_letter_switch(new_unit)
    
    return new_unit
    
def find_rotations(queen_locations):
    
    all_locations = [queen_locations]
    #Rotated Across
    
    rotated_across_locations = []
    
    for locations in queen_locations:
        letter = find_opposite(locations[0])
        number = find_opposite(locations[1])
        rotated_across_locations.append([letter, number])
    
    all_locations.append(rotated_across_locations)
    #Rotated to the left
    
    rotated_right_locations = []
    
    for locations in queen_locations:
        letter = num_letter_switch(find_opposite(locations[1]))
        number = num_letter_switch(locations[0])
        rotated_right_locations.append([letter, number])
        
    all_locations.append(rotated_right_locations)
    
    
    #Rotated to the right
    
    rotated_left_locations = []
    
    for locations in queen_locations:
        letter = num_letter_switch(locations[1])
        number = num_letter_switch(find_opposite(locations[0]))
        rotated_left_locations.append([letter, number])
    
    all_locations.append(rotated_left_locations)
    
    return all_locations
    

solutions = []
info_copy = deepcopy(info)
solution = 0

i = 0
all_other_locations = []

while len(info) > 0 and i < 2000:
      #checks that it wont run on forever
    i += 1
    non_mirrored_locations = find_rotations(info[0])
    solution = non_mirrored_locations[0]
    solutions.append(solution)
    
    for l in non_mirrored_locations:
        all_other_locations.append(sort_queens(l))
    
    mirrored_placements = []
    for placements in info[0]:
        letter = find_opposite(placements[0])
        #number = placements[1]
        mirrored_placements.append([letter, placements[1]])
            
    mirrored_locations = find_rotations(mirrored_placements)
    
    for l in mirrored_locations:
        all_other_locations.append(sort_queens(l))
       
    for location in all_other_locations:
       for queen_placement in info:
           if queen_placement == location:
                info.remove(location)
                
print(f"Final Solutions: {len(solutions)}")
print("\n")

for s in solutions:
    print(s)
    print("\n")

        
            
        
            
    
    

        