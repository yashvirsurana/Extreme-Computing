#!/usr/bin/python

import sys

for line in sys.stdin:

    line = line.strip()
    line = line.split()
    print line[0], line[1]