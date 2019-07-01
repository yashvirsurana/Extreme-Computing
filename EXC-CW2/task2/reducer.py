#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET
import heapq as hp

top10 = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

hp.heapify(top10)
number = 0

for line in sys.stdin:
	
	line = line.strip()
	line = line.split()
	line = map(int, line)
	if line[0] > top10[0][0]:
		hp.heappushpop(top10, (line[0], line[1]))
		
final = top10.sort(reverse=True)
for x in top10:
	print x[0], x[1]
















