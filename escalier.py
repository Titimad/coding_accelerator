#!/usr/bin/python3
import sys
nombre_marches = int( sys.argv[1] )
print(nombre_marches)
for i in range(nombre_marches):
    string = ' ' * (nombre_marches + 1 - i) + '#' * (i + 1)
    print (string)

