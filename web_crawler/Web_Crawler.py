# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:15:11 2021

@author: ryder
"""

import requests
import time
from copy import deepcopy

used_links = []

def find_all_links(web_address):
    global used_links
    website = requests.get(web_address)
    read_website = website.text
    read_website = read_website.split('<')
    code_for_links = []
    for line in read_website:
        try:
            if line[0] == 'a':
                code_for_links.append(line)
        except:
            pass
    
    #Gets rid of any code that isn't a link
    links = []
    for link in code_for_links:
        link = link.split('"')
        actual_link = list(str(link[1]))
        word_check = ""
        for letter in actual_link[0:4]:
            word_check = word_check + letter
        if(word_check != "http"):    
            for characters in actual_link:
                if characters == '/':
                    links.append(link[1])
                    break
    
    for link in range(len(links)):
        links[link] = f'https://www.helloworldstudio.org{links[link]}'
            
    copy = deepcopy(links)
            
    if len(used_links) != 0:        
        for link in copy:
            for l in used_links:
                if l == link:
                    links.remove(link)
                    break
    
    for link in links:
        used_links.append(link)
        
    used_links = list(set(used_links))
            
    links = list(set(links))
    copy = list(set(copy))
    time.sleep(3)
    return links, copy

linked_links = {}
linked_links
new_links, all_links = find_all_links('https://www.helloworldstudio.org')
while len(new_links) > 0:
    newer_links, linked_links[new_links[0]] = find_all_links(new_links[0])
    if len(newer_links) != 0:
        for link in newer_links:
            new_links.append(link)
    new_links.remove(new_links[0])
    print(new_links)
    
    
    
    
for link in new_links[:]:
    new_links , linked_links[link] = find_all_links(link)
    

    
    
    
            


