#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	line = line.strip()
	pre = line.split('-->')
	name = pre[0]
	marks = re.findall(r'(?<=,)[0-9][0-9][0-9]|(?<=,)[0-9][0-9]|(?<=,)[0-9]',pre[1])


 	if len(marks)>3:
		avg = float(sum(map(int, marks)))/float(len(marks))
	else:
		avg = 0.0

	print (name+'\t'+str(avg))
