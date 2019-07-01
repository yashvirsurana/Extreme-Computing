from random import Random
import math


class BloomBloom:
	# Reference: http://en.wikipedia.org/wiki/Bloom_filter
	# Reference: https://corte.si/posts/code/bloom-filter-rules-of-thumb/index.html

	def __init__(self, num_lines, text):
		self.num_bytes = int(math.ceil(num_lines*math.log(1/0.0099)/(math.log(2)*math.log(2)))) 
		self.array = [0] * self.num_bytes #bytearray(self.num_bytes)
		self.num_hashes = int(math.ceil(self.num_bytes/num_lines*math.log(2)))
		#self.update(text)

	def get_hashes(self, line):
		return (int(hash(str(i)+'_'+line)%self.num_bytes) for i in range(self.num_hashes))

	def update(self, text):
		for line in text:
			line = line.strip()
			for i in self.get_hashes(line):
				self.array[i] = 1#self.array[i] or 1

	def updateL(self, line):
		line = line.strip()
		for i in self.get_hashes(line):
			self.array[i] = 1#self.array[i] or 1

	def __contains__(self, line):
		return all(self.array[i] for i in self.get_hashes(line))






