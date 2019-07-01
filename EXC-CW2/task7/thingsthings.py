#!/usr/bin/python

import sys
import math

if(len(sys.argv) != 1):
    print "please enter only 1 parameter, the number of lines"
no_lines = int(sys.argv[1])


bit_vector_array = []

p = 0.0099

bits_per_key = int(math.ceil(- math.log(p, 2) / math.log(2)))
no_bits = no_lines * bits_per_key


no_hashes = int(math.ceil((no_bits / no_lines) * math.log(2)))


print(no_lines)
print(bits_per_key)
print(no_bits)
print(no_hashes)

##initialise bit vector array to false
for i in range(no_bits):
    bit_vector_array.append(0)


def get_hashed_indexes(line):
    hash_index_list = []

    for i in range(no_hashes):
        concated_line = str(i) + line
        bit_position = hash(concated_line) % no_bits
        hash_index_list.append(bit_position)

    return hash_index_list

def query(line):

    hash_index = get_hashed_indexes(line)
    bools = []
    for x in hash_index:
        bools.append(bit_vector_array[x])

    if(all(bools)):
        return True
    else:
        return False

def insert(line):
    line=line.strip()
    hash_list = get_hashed_indexes(line)
    for i in hash_list:
        bit_vector_array[i] = 1


faggot = 0
for line in sys.stdin:
    line = line.strip()


    
    if(query(line)):
        continue
    else:
        print line
        insert(line)
        faggot +=1

    
print "sahiofeifhoeihfoihafoiasdhoidfhsiphsdf : ", faggot
