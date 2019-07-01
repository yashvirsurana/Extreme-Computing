#!/usr/bin/env python

import sys
import math
# Reference : http://www.vldb.org/conf/2002/S10P03.pdf
error = 0.001
width = int(math.ceil(1.0/error))
b_current = 1 
data = {}
N = 0
threshold = 0.01

# N, b_current, f are runnning variables

#element : (f, delta) delta starts with b_current -1

for element in sys.stdin:
	element = element.strip()
	N += 1
	b_current = math.ceil(N/width)
	if data.get(element)==None:
		data[element] = [1, b_current-1]
	else:
		data[element][0] += 1
	if (N % width) == 0:
		for key in data.keys():
			if (data[key][0]+data[key][1])<= b_current:
				del data[key]

final = N*(threshold-error)

for key in data.keys():

	if (data[key][0]>=final):
		print key














