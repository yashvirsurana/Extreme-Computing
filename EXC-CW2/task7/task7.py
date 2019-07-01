from bloom import *
import sys
#95350
if (__name__ == "__main__"):
	
	num_lines = int(sys.argv[1])

with open('/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webSmall.txt', 'r') as web:

	bb = BloomBloom(num_lines, web)
	
	for line in web:
		line = line.strip()

		if line in bb:
			continue
		else:
			print line
			bb.updateL(line)
			
