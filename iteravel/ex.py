"""
iteravel, iteraveis, geradores
"""
import sys
import time


l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))

for v in l2:
    print(v)