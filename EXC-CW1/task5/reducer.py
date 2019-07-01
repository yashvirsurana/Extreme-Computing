#!/usr/bin/python

import sys

index = 0;

for line in sys.stdin:
    if index < 20:
        index = index + 1
        line = line.strip()
        line = line.split('\t')
        key = line[0]
        key = 999999999 - int(key)
        print line[1]+'\t'+str(key)
        
