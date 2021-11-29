import codecs
import random
import pandas as pd

#creates a dictionary for id and emojis
emoji_locator = {}
data_frame = pd.read_csv("emoji_lookup.tsv", delimiter = "\t", header = None)
for i in range(len(data_frame[0])):
    emoji_locator[str(data_frame[0][i])] = str(data_frame[1][i])
    
#find the distance from the origin 
def distance_from(list_1, *list_2):
    for coordinates in list_2:
        distance = 0
        i = 1
        while i < num_dimensions:
            distance = distance + (float(list_1[i]) - coordinates[i])**2
            if i > 500:
                break;
            i = i + 1
        distance = distance**(1/2)
        
        return distance

def create_centroid():
    
    random_dimension = [random.uniform(-0.01, 0.01) for i in range(num_dimensions)] 
    return random_dimension
        
from collections import defaultdict 
#find a list within a list

def center_centroids(dictionary):
    #Sorts it into a dictionary
    emojis_near_centroid = ''
    res = defaultdict(list)
    for key, val in sorted(dictionary.items()):
        res[val].append(key)
    emojis_near_centroid = dict(res)
    
    centroids = {}
    
    for i in range(len(centroid_list)):
        list_sum = []
        for coordinate in range(len(emoji_dictionary['eoji1f602'])):
            coordinate_list = []
            for emoji in emojis_near_centroid[i]:
                coordinate_list.append(float(emoji_dictionary[emoji][coordinate]))
            list_sum.append(sum(coordinate_list) / len(emojis_near_centroid[i]))
        list_sum.insert(0, 'dummy_value')
        centroids[i] = list_sum
    return centroids


def find_closest_centroid():
    closest_centroid = {}
    for line in content_string:
        centroid_distance_list = []
        for centroids in centroid_list:
            centroid_distance_list.append(distance_from(line, centroids))#
            
        closest_centroid = centroid_distance_list.index(min(centroid_distance_list))
        closest_centroid_dictionary[line[0]] = closest_centroid
    return center_centroids(closest_centroid_dictionary)
    
    
file_object = codecs.open('Emoji_Code.txt', 'r', encoding='utf8', errors='ignore')

content_string = file_object.read()

file_object.close()

content_string = content_string.splitlines()

closest_centroid_dictionary = {}

#splitting the lines and getting rid of the first line
for index, value in enumerate(content_string):
    content_string[index] = value.split()
content_string.remove(content_string[0])

#organizing the list into a dictionary
emoji_dictionary = {}
for items in content_string:
    emoji_type = items[0]
    emoji_dictionary[emoji_type] = items[1:]
    
    
    
#getting number of dimensions 
num_dimensions = len(content_string[0])
origin = []
for i in range(num_dimensions):
    origin.append(0)

#Makes The Centroid
centroid_list = []
for i in range(15):
    centroid = create_centroid()
    centroid_list.append(centroid)




#compares data points with the centroids and then finds the average 
for iteration in range(16):
    new_closest_centroid = find_closest_centroid()
    for i in range(len(centroid_list)):
        centroid_list[i] = new_closest_centroid[i]  
    empty_list = []
        
    if iteration == 15:
        for i in range(len(centroid_list)):
            emoji_list = []
            for key, value in closest_centroid_dictionary.items():
                if(value == i):
                    emoji_list.append(str(emoji_locator[key[4:]]))
            print(str(i) + ": ", end = "")
            print(emoji_list, end = " ")
            print("\n")
                    
        
        
        
    

    
