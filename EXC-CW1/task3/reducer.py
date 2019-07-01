#!/usr/bin/python

import sys

tokenlen=0
linelen=0
for line in sys.stdin:
	line=line.strip()
	line=line.split(' ')
	if int(line[0])>tokenlen:
		tokenlen=int(line[0])
	if int(line[1])>linelen:
		linelen=int(line[1])
print (str(tokenlen) + ' ' + str(linelen))