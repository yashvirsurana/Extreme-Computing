#!/usr/bin/python
import sys

firstLine = sys.stdin.readline().strip()
tmp = firstLine.split()

prevWord = tmp[0]
prevFile = tmp[1]
count = 1
for line in sys.stdin:
    
    line = line.strip()
    line = line.split()

    currentWord = line[0]
    currentFile = line[1]

    cond1 = currentWord==prevWord 
    cond2 = currentFile== prevFile
    if cond1:

    	if cond2:
    		count += 1
    	else:
    		print prevWord, prevFile, count
    		prevFile = currentFile
    		count = 1
    else:
    	print prevWord, prevFile, count
    	prevFile = currentFile
    	prevWord = currentWord
    	count = 1
print prevWord, prevFile, count












