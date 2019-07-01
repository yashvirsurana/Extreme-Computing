#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET
import heapq as hp

#top10 = []
top10 = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]


hp.heapify(top10)
number = 0

for line in sys.stdin:
	
	line = line.strip()

	row = ET.fromstring(line)

	if row.attrib['PostTypeId']=='1':
		"""
		number += 1
		if number<11:
			hp.heappush(top10, (row.attrib['ViewCount'], row.attrib['Id']))
		
		else:
		"""
		if int(row.attrib['ViewCount'])>top10[0][0]:
			hp.heappushpop(top10, (int(row.attrib['ViewCount']), int(row.attrib['Id'])))

for x in top10:
	print x[0], x[1]
