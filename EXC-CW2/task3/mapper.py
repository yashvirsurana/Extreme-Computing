#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET



for line in sys.stdin:
	
	line = line.strip()

	row = ET.fromstring(line)

	if row.attrib['PostTypeId']=='2':

		print row.attrib['OwnerUserId'], row.attrib['ParentId']




