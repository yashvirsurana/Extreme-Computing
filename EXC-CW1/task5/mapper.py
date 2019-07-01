#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	line = line.split('\t')

	key = 999999999-int(line[1])  

	print str(key)+'\t'+line[0]
