#!/usr/bin/python3

import sys

print (sys.argv)
liste = sys.argv[1:]
liste.sort(reverse=True)
string = " ".join(liste)
print (string)
