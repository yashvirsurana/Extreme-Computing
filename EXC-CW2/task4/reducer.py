#!/usr/bin/python

import sys

temp = sys.stdin.readline().strip().split()

currentId = ''

if len(temp)==2:
	currentId = temp[0]

for line in sys.stdin:
	line = line.strip()
	row = line.split()

	if len(row)==2:
		currentId=row[0]
	else:
		if currentId==row[0]:
			print row[1], row[0]






