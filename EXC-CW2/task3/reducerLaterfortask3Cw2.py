#!/usr/bin/python
import sys

firstLine = sys.stdin.readline().strip()
tmp = firstLine.split(' ')

prevUsersPosts = tmp[1:]
prevCount = len(prevUsersPosts)
prevUser = tmp[0]

maxUsersPosts = tmp[1:] 
maxCount = len(maxUsersPosts)
maxUser = tmp[0]

for line in sys.stdin:
	
	line = line.strip()
	line = line.split(' ')

	currentUsersPosts = line[1:]
	currentCount = len(currentUsersPosts)
	currentUser = line[0]
	if currentUser == prevUser:
		prevUsersPosts = ' '+currentUsersPosts
		currentCount += prevCount
	else:
		if currentCount > maxCount:
			maxCount = currentCount
			maxUsersPosts = prevUsersPosts
			maxUser = prevUser
		prevUser = currentUser
		prevUsersPosts = currentUsersPosts
		prevCount = currentCount

print maxUser+' -> '+ str(maxUsersPosts)[1:][:-1]


