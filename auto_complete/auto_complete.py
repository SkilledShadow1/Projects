#TODO format the code so it repeats multiple times and stop repeating answers
import codecs

#Getting the file and reading it
history_file = codecs.open('my_history.txt', 'r', 
                          encoding='utf8', errors='ignore')
history_text = history_file.read()
history_file.close()

#Splitting the text by lines and then splitting the lines
history_text = history_text.splitlines()
split_searches = []
for searches in history_text:
    searches = searches.split()
    split_searches.append(searches)

#user input
print('You can only type in full words not parts of them')

while True:
    formatting = input('Do you want to search by word or by letter? type w or l')
    if formatting == 'l' or formatting == 'w':
        break
    else:
        print('type either l or w')
    
sentence = input('Type in a word or phrase that you want to be autocompleted ')
if formatting == 'l':
    sentence = str(sentence)
    sentence = list(sentence)
    
if formatting == 'w':
    sentence = sentence.split()

possible_searches = []


#these will be the completing searches
for searches in split_searches: 
    if formatting == 'l':
        searches = ' '.join(searches)
        searches = str(searches)
        searches = list(searches)
    for word in range(len(sentence)):
        if searches[word] != sentence[word]:
            break
        if word == len(sentence) - 1:
            possible_searches.append(searches)

#removes same search from the list      
if len(possible_searches) > 1:
    for i in range(len(possible_searches)):
        sentence_to_check = possible_searches.pop(0)
        for searches in possible_searches:
            if sentence_to_check == searches:
                break
            if searches == possible_searches[-1]:
                possible_searches.append(sentence_to_check)
        
        
def add_to_trie(search, trie, search_value):
    
    if(search_value > len(search) - 1):
        return search_value
    
    #checks repreating words and adds value if repreating
    for dictionary in trie['children']:
        if dictionary['value'] == search[search_value]:
            dictionary['count'] += 1
            add_to_trie(search, dictionary, search_value + 1)
            return
    
    #adds a new word to the children
    new_word = {}
    new_word['value'] = search[search_value]
    new_word['count'] = 1
    new_word['used'] = 0
    new_word['children'] = []
    trie['children'].append(new_word)
    add_to_trie(search, new_word, search_value + 1)
    
def auto_complete(trie, possible_answer, end):
    
    
    possible_answer.append(trie['value'])
    
    #checking to see if there is the same text but shorter so it is not left out
    counter = 0
    for dictionary in trie['children']:
        if dictionary['used'] >= dictionary['count']:
            counter += 1
            
    if trie['children'] == [] or counter >= len(trie['children']):
        if formatting == 'w':
            possible_answer = ' '.join(possible_answer)
        if formatting == 'l':
            possible_answer = ''.join(possible_answer)
        top_5_searches.append(possible_answer)
        return
    
        
    for children in trie['children']:
        if(children['used'] < children['count']):
            children['used'] += 1
            auto_complete(children, possible_answer, end)
    
start_trie = {'value' : '^', 'count' : 0, 'used' : 0, 'children' : []}

def get_words(search, top_5_searches):
    start_trie['count'] += 1
    add_to_trie(search, start_trie, 0)
    auto_complete(start_trie, [], False)
    
        
top_5_searches = []
for search in possible_searches:
    get_words(search, top_5_searches)

#sorts by recent searches
for searches in top_5_searches[:5]:
    print(searches[1:])

if(len(top_5_searches) == 0):
    print('I could not find any searches starting with this word or phrase')
    
#possible_answer = []
#auto_complete(start_trie, possible_answer, end = False)
#this will find most popular searches and print out ones that have less than 5




