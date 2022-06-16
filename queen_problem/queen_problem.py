import random
from copy import deepcopy

board_size = int(input("What do you want the board size to be"))

def create_board(board_size):
    board_list = []
    
    for tile in range(board_size):
        row = []
        board_list.append(row)
        
    for rows in board_list:
        for tile in range(board_size):
            rows.append(True)
    
 
    return board_list
          
     
def sort_queens(queen_coordinates):
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    sorted_list = sorted_list[:board_size]
    s_list_copy = deepcopy(sorted_list)
    for coordinate in queen_coordinates:
        for letter in sorted_list:
            if coordinate[0] == letter:
                s_list_copy[s_list_copy.index(letter)] = coordinate
                
    return s_list_copy
       
def randomize_queens(board_size, set_letter):
    can_work = False
    trys = 0
    while can_work == False:
        number_letter_dictionary = {}
        letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        
        if board_size < 12:
            letters = letters[:board_size]
            numbers = numbers[:board_size]

        for number in numbers:
            number_letter_dictionary[number] = letters[:]
        
        queen_list = []
        will_work = True
        for tile in range(board_size):
            queen_number = board_size - tile
            if len(number_letter_dictionary[queen_number]) != 0:
                if queen_number != board_size:
                    queen_letter = random.choice(number_letter_dictionary[queen_number])
                if queen_number == board_size:
                    queen_letter = set_letter
            else:
                will_work = False
                break
            number_letter_dictionary = go_through_diagonal(queen_letter, queen_number, number_letter_dictionary)
            queen_list.append((queen_letter, queen_number))
            number_letter_dictionary
        
        
        trys += 1
        if trys > 100:
            return ['']
        if will_work == True:
            can_work = True
            
            queen_list = sort_queens(queen_list)
            
            q_list = []
            for item in queen_list:
                q_list.append((num_to_letter(item[0]), item[1]))
                
            return q_list
    
def go_through_diagonal(current_letter, current_num, dictionary):
    
    cl = current_letter
    cn = current_num
    
    while current_letter < (board_size) and current_num > 1:
        current_letter += 1
        current_num -= 1 
        for value in dictionary[current_num]:
            if value == current_letter:
                dictionary[current_num].remove(current_letter)
                
    current_letter = cl
    current_num = cn    
    
    while current_letter > 1 and current_num > 1:
        current_letter -= 1
        current_num -= 1 
        for item in dictionary[current_num]:
            if item == current_letter:
                dictionary[current_num].remove(current_letter)

    current_letter = cl
    current_num = cn 
    
    for key in dictionary:
        for value in dictionary[key]:
            if value == current_letter:
                dictionary[key].remove(current_letter)
    return dictionary

def num_to_letter(num):
    if num == 1:
        num = 'a'
        
    elif num == 2:
        num = 'b'
    
    elif num == 3:
        num = 'c'
        
    elif num == 4:
        num = 'd'
        
    elif num == 5:
        num = 'e'
        
    elif num == 6:
        num = 'f'
        
    elif num == 7:
        num = 'g'
        
    elif num == 8:
        num = 'h'
    
    elif num == 9:
        num = 'i'
        
    elif num == 10:
        num = 'j'
        
    elif num == 11:
        num = 'k'
        
    elif num == 12:
        num = 'l'
    
    return num
 
similar_counter = 0

answer_list = []

trys = 0
max_tries = 300
set_letter = 1

if board_size > 8:
    max_tries = max_tries * (2 ** (board_size - 8))
    max_tries = int(max_tries)
#Checks for tries in a row
while set_letter < board_size + 1:
    while trys < max_tries:        
        board = create_board(board_size)
        randomized_queens = randomize_queens(board_size, set_letter)
    
        will_add = True
        for q in answer_list:
            if q == randomized_queens:
                will_add = False
                
        if will_add:
            trys = 0
            answer_list.append(randomized_queens)
        
        trys += 1
       
    set_letter += 1
    trys = 0

new_answer_list = []

for a in answer_list:
    if a == ['']:
        answer_list.remove([''])
    
import json




print(f"All Solutions: {len(answer_list)}")
print("\n")
for answer in answer_list:
    print(answer)
    print("\n")

with open('queen_placement.json', 'w') as json_file:
    json.dump(answer_list, json_file)
    
    
    
    