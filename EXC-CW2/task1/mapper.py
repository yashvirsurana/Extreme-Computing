#!/usr/bin/python
import sys
import os


filename = os.environ["mapreduce_map_input_file"]
filename = os.path.basename(filename)
#filename = "pizza.txt"
for line in sys.stdin:
    
    line = line.strip()
    line = line.split()
    #line = map(lambda x:(x,1), line)
    for x in line:
    	print x, filename, 1
