#!/usr/bin/python3

import sys

#ouvrir le fichier source

word1 = sys.argv[1]
fichier1 = open(sys.argv[2], 'r')

list_words = fichier1.readlines()

list_result = []
list_char1 = list(word1)
list_char1.sort()

for word in range(len(list_words)):
    
    list_words[word] = list_words[word][0:len(list_words[word]) - 1]
    
    list_char2 = list(list_words[word])
    list_char2.sort()
    
    if list_char1 == list_char2:
        list_result.append(list_words[word])

print(list_result)

fichier1.close()
