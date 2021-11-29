import random
from copy import deepcopy
from termcolor import colored
#from termcolor import colored

def split_word(word):
    return [char for char in word]

def get_backwards(word):
    reversed_string = ''
    reversed_string =''.join(reversed(word))
    return reversed_string
    
    
def create_box():
    """Creates the size of the box for the word search"""
    
    text_file ='word_search.txt'
    word_file = open(text_file)

    word_list = word_file.readlines()
    words = []
    for line in word_list:
        line = line.replace('\n', '')
        line = line.upper()
        words.append(line)
    
    parameter_list = []
    parameter_list.append(words[0])
    parameter_list.append(words[1])
    
    words = words[2:]
    print("\n")
    word_search_list = []
    for parameter_num in range(int(parameter_list[0])):
        row = []
        word_search_list.append(row)
    
    for rows in word_search_list:
        for letter_num in range(int(parameter_list[1])):
           rows.append(True)
        
    return word_search_list, parameter_list, words,
    
def format_word():
    list1 = [0, 1, 2]
    list2 = [0, 1]
    word_type = random.choice(list1) #Horizontal, Veritcal, Diagonal
    word_orientation = random.choice(list2) #Forwards, Backwards
    return word_type, word_orientation
    
def get_start_pos(parameter_list):
    
    start_pos = ()
    
    row_list = []
    for row in range(int(parameter_list[0])):
        row_list.append(row)
    
    column_list = []
    for column in range(int(parameter_list[1])):
        column_list.append(column)
    
    start_pos = (random.choice(row_list), random.choice(column_list))
    return start_pos
    

def does_it_fit(word, parameter_list, box_outline):
    
    word_type, word_orientation = format_word()
    
    taken_up_list = deepcopy(box_outline)
    
    start_pos = get_start_pos(parameter_list)
    
    if word_orientation == 1:
        word = get_backwards(word)
        
    if word_type == 0: #Horizontal
        for i in range(len(word)):
            next_column = start_pos[1] + i 
            if next_column > int(parameter_list[1]) - 1:
                return False, box_outline
            if box_outline[start_pos[0]][next_column] != True:
                return False, box_outline
    
            taken_up_list[start_pos[0]][next_column] = word[i]
            
    if word_type == 1: #Vertical
        for i in range(len(word)):
            next_row = start_pos[0] + i
            if next_row > int(parameter_list[0]) - 1:
                return False, box_outline
            if box_outline[next_row][start_pos[1]] != True:
                return False, box_outline
            
            taken_up_list[next_row][start_pos[1]] = word[i]

    if word_type == 2: #Diagonal
        for i in range(len(word)):
            next_row = start_pos[0] + i
            next_column = start_pos[1] + i
            if next_row > int(parameter_list[0]) - 1:
                return False, box_outline
            if next_column > int(parameter_list[1]) - 1:
                return False, box_outline
            if box_outline[next_row][next_column] != True:
                return False, box_outline

            taken_up_list[next_row][next_column] = word[i]

    return True, taken_up_list


def does_it_fit_answer(word, parameter_list, box_outline):
    
    word_type, word_orientation = format_word()
    
    taken_up_list = deepcopy(box_outline)
    
    start_pos = get_start_pos(parameter_list)
    
    if word_orientation == 1:
        word = get_backwards(word)
        
    if word_type == 0: #Horizontal
        for i in range(len(word)):
            next_column = start_pos[1] + i 
            if next_column > int(parameter_list[1]) - 1:
                return False, box_outline
            if box_outline[start_pos[0]][next_column] != True:
                return False, box_outline
    
            taken_up_list[start_pos[0]][next_column] = colored(word[i],"white", "on_red")
            
    if word_type == 1: #Vertical
        for i in range(len(word)):
            next_row = start_pos[0] + i
            if next_row > int(parameter_list[0]) - 1:
                return False, box_outline
            if box_outline[next_row][start_pos[1]] != True:
                return False, box_outline
            
            taken_up_list[next_row][start_pos[1]] = colored(word[i],"white", "on_red")

    if word_type == 2: #Diagonal
        for i in range(len(word)):
            next_row = start_pos[0] + i
            next_column = start_pos[1] + i
            if next_row > int(parameter_list[0]) - 1:
                return False, box_outline
            if next_column > int(parameter_list[1]) - 1:
                return False, box_outline
            if box_outline[next_row][next_column] != True:
                return False, box_outline

            taken_up_list[next_row][next_column] = colored(word[i], "white", "on_red")

    return True, taken_up_list


box_outline, parameter_list, words_list = create_box()
for word in words_list:
    fit = False
    l = 0
    while fit == False:
        fit, taken_up_list = does_it_fit(str(word), parameter_list, box_outline)
        l = l + 1
        box_outline = deepcopy(taken_up_list)
        
        if(l > 20):
            print("Nice job. You made the borders too small for your words.")
            break
        
        
common_letters = "a b c d e f g h i l m n o p r s t u w y"
common_letters = common_letters.upper()
common_letters = common_letters.split()       
        
for row in range(int(parameter_list[0])):
    for column in range(int(parameter_list[1])):
        if box_outline[row][column] == True:
            box_outline[row][column] = random.choice(common_letters)

print('Word Bank: \n'.center(120))

i = 0
print(' '.center(35), end = ' ')
for word in words_list:
    print(word, end='  ')
    i = i + 1
    if(i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30):
        print('')
        print(' '.center(36), end = '')

print('\n')

for row in box_outline:
    print('')
    print(' '.center(36), end = '')
    for letter in row:
        print(letter, end='  ')

print('\n')





box_outline, parameter_list, words_list = create_box()
for word in words_list:
    fit = False
    l = 0
    while fit == False:
        fit, taken_up_list = does_it_fit_answer(str(word), parameter_list, box_outline)
        l = l + 1
        box_outline = deepcopy(taken_up_list)
        if(l > 100):
            print("Nice job. You made the borders too small for your words.")
            break
