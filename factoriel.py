#!/usr/bin/python3

import sys

nombre = int(sys.argv[1])
result = 1

for i in range(1, nombre+1):
    result = i * result
print(result)
