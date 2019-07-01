#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET


for line in sys.stdin:
	
	line = line.strip()


	row = ET.fromstring(line)

	if row.attrib['PostTypeId']=='1':
		if 'AcceptedAnswerId' in row.attrib:
			print row.attrib['AcceptedAnswerId'], 1

	if row.attrib['PostTypeId']=='2':
		print row.attrib['Id'], row.attrib['OwnerUserId'], 1

