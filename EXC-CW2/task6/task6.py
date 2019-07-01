#!/usr/bin/env python

import sys
import random

result = []
counter = 0

#with open('/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt', 'r') as text:

for line in sys.stdin:

	line = line.strip()

	if len(result)<100:
		result.append(line)
	else:
		rand = int(random.random() * counter)
		if rand < 100:
			result[rand] = line
	counter += 1

for x in result:
	print x
