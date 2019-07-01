#!/usr/bin/python

import sys

highAvgs = [0]
highNames = []

for line in sys.stdin:
	line = line.strip()
	line = line.split('\t')
	if (line[1]==highAvgs[0] and line[1] != '0.0'):
		highAvgs = [line[1]] + highAvgs
		highNames = [line[0]] + highNames
	if line[1]>highAvgs[0]:
		highNames = [line[0]]
		highAvgs = [line[1]]
	
	"""
	if len(line)>4:
		name = line[0]
		avg = float(sum(map(int, line[1:]))/(len(line)-1))
		if avg>highAvg:
			highName = name
			highAvg = avg
	"""
for x in range(0,len(highAvgs)):
	print highNames[x]+'\t'+highAvgs[x]
