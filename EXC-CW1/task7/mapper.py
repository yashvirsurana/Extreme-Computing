#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	line = line.split()
	if (len(line)==3): # table name is student
		print (line[1]+'\t'+line[2])
	elif (len(line)==4): # table name is marks
		print (line[1]+'\t'+line[2]+'\t'+line[3])
		