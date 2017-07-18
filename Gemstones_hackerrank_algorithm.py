#!/bin/python

import sys

def gemstones(arr):
    # Complete this function
    gemArr = []
    hashTable = {}
    for i in arr:
        gemArr.append(list(i))
    for element in gemArr:
        for letter in element:
            hashTable[hash(letter)] = letter
    for 
    return hashTable

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)