#!/usr/bin/python

import sys

temp = sys.stdin.readline().strip().split()

prevOwner = temp[0]
prevAns = temp[1]
prevCount = 1

maxOwner = temp[0]
maxAns = temp[1]
maxCount = 1

for line in sys.stdin:
	line = line.strip()
	row = line.split()

	if row[0]==prevOwner:
		thing = ', '+row[1]
		prevAns += thing
		prevCount += 1

	else:
		if prevCount>maxCount:
			maxOwner = prevOwner
			maxAns = prevAns
			maxCount = prevCount
		prevOwner = row[0]
		prevAns = row[1]
		prevCount = 1

print maxOwner + ' -> ' + str(maxCount) + ', '+ maxAns

