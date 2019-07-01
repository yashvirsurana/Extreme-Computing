#!/usr/bin/python
import sys

firstLine = sys.stdin.readline().strip()
tmp = firstLine.split()

prevUser = tmp[0]
prevPosts = tmp[1]
prevCount = 1

maxUser = tmp[0]
maxPosts = tmp[1]
maxCount = 1

for line in sys.stdin:
	
	line = line.strip()
	line = line.split()

	currentUser = line[0]
	currentPost = line[1]

	if currentUser==prevUser:
		prevCount += 1
		prevPosts += ', '+currentPost
	else:
		if prevCount>maxCount:
			maxUser = prevUser
			maxPosts = prevPosts
			maxCount = prevCount
		prevUser = currentUser
		prevPosts = currentPost
		prevCount = 1
print maxUser+' -> '+maxPosts



