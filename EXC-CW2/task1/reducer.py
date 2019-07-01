#!/usr/bin/python
import sys

firstLine = sys.stdin.readline().strip()
tmp = firstLine.split()

prevWord = tmp[0]
count = 1
stats = '('+tmp[1]+', '+str(tmp[2])+')' 

for line in sys.stdin:
    
    line = line.strip()
    line = line.split()

    currentWord = line[0]

    if currentWord==prevWord:
    	thing = ', ('+line[1]+', '+str(line[2])+')'
    	stats += thing
    	count += 1

    else:
    	print prevWord+'\t:\t'+str(count)+'\t:\t'+'{'+stats+'}'
    	prevWord = currentWord
    	count = 1 
    	stats = '('+line[1]+', '+str(line[2])+')'
print prevWord+'\t:\t'+str(count)+'\t:\t'+'{'+stats+'}'


