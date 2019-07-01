#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    print max(map(len,line.split(' '))),len(line)