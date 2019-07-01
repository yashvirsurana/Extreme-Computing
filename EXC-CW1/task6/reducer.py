#!/usr/bin/python

import sys
import math
import re

for line in sys.stdin:
	line = line.strip()
	line = line.split('\t')
	entropy = 0.0
	context = line[0]
	totalcount = float(line[1])
	instances = line[2]
	instances = re.findall(r'\d+', instances)#re.findall(r'[0-9][0-9]|[0-9]', instances)

	for x in instances:
		entropy += (-1)*float(x)/totalcount*math.log((float(x)/totalcount), 2.0)

	print context+'\t'+str(entropy)