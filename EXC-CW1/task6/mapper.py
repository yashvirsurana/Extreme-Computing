#!/usr/bin/python

import sys

prevLine = sys.stdin.readline().strip().split()
prevContext = prevLine[:2]
currentSum = int(prevLine[3])
currentCounts = [int(prevLine[3])]

for line in sys.stdin:
	line = line.strip()
	line = line.split()

	current = line[:2]
	count = int(line[3])

	if current==prevContext:
		currentSum += count
		currentCounts.append(count)
	else:
		print prevContext[0]+' '+prevContext[1]+'\t'+str(currentSum)+'\t'+str(currentCounts)
		prevContext = current
		currentSum = int(count)
		currentCounts = [int(count)]
	
print current[0]+' '+current[1]+'\t'+str(currentSum)+'\t'+str(currentCounts)
