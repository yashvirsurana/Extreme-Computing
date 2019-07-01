#!/usr/bin/python

import sys

firstLine = sys.stdin.readline().strip()
tmp1 = firstLine.split(',')
prevLine = tmp1[0]
count = int(tmp1[1])

for line in sys.stdin:
	line = line.strip()
	tmp2 = line.split(',')
	sequence = tmp2[0]
	counter = tmp2[1]

	if (sequence != prevLine):
		print(prevLine+'\t'+str(count))
		prevLine = sequence
		count = int(counter)
	else:
		count = count + int(counter)

if (prevLine==sequence):
	print(sequence+'\t'+str(count))
