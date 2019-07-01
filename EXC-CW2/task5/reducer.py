#!/usr/bin/env python

import sys
import random

firstLine = sys.stdin.readline().strip()
temp = firstLine.split('\t')

theLine = temp[0]
theP = int(temp[1])

for line in sys.stdin:
	line = line.strip()
	line = line.split('\t')

	currentLine = line[0]
	currentP = int(line[1])

	theP += currentP

	if random.randint(0, theP)<currentP:

		theLine = line[0]
	

print theLine


