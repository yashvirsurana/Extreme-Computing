#!/usr/bin/python

import sys

temp = sys.stdin.readline().strip().split()
currentKey = temp[0]
output = ''
if temp[0]==currentKey:
		#if length is 2 it is name
	if len(temp)==2:
		output = temp[1] + '-->' + output
	elif len(temp)==3:
		output = output+'('+temp[1]+','+temp[2]+') '

for line in sys.stdin:
	line = line.strip()
	data = line.split()

	if data[0]==currentKey:

		#if length is 2 it is name
		if len(data)==2:
			output = data[1] + '-->' + output
		elif len(data)==3:
			output = output+'('+data[1]+','+data[2]+') '
	
	if data[0]!=currentKey:
		print output
		output = ''
		currentKey = data[0]
		#if length is 2 it is name
		if len(data)==2:
			output = data[1] + '-->' + output
		elif len(data)==3:
			output = output+'('+data[1]+','+data[2]+') '
print output