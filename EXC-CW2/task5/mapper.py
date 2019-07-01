#!/usr/bin/env python

import sys
import random

line_number = 0
resevoir = ''

for line in sys.stdin:
	line = line.strip()

	if random.randint(0, line_number) == 0:

		resevoir = line

	line_number += 1

print resevoir+'\t'+str(line_number)








