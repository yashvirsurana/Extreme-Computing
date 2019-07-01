#!/usr/bin/python

import sys

for line in sys.stdin:
	line=line.strip()
	words=line.split(' ')
	
	for i in range(0,len(words)-2):
		seq=words[i]+' '+words[i+1]+' '+words[i+2]
		print seq+','+str(1)