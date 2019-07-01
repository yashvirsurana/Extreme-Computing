#!/usr/bin/python

import sys
prev_line= ''

for line in sys.stdin:
	line = line.strip()
	if line == prev_line:
		continue
	else:
		prev_line = line
		print line	
