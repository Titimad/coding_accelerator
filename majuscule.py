#!/usr/bin/python3

import sys

#string = sys.argv[1]
string = input()
result = ""
rang_lettre = 1
string = string.lower()
for i in range(len(string)):
    
    if string[i].isalpha() and rang_lettre == 0:
            result = result + string[i].upper()
            rang_lettre = 1
    elif string[i].isalpha() and rang_lettre == 1:
            result = result + string[i]
            rang_lettre =0
    else:
        result = result + string[i]

print (result)
        
