'''
Transform a Freemind mindmap file to a json array. 
'''
import sys
import xml
import json

from xml.etree.ElementTree import XMLParser
import xml.etree.ElementTree as ET

file = sys.argv[1]

nodes = []
with open(file, 'r') as content_file:
	content = content_file.read()
	e = ET.fromstring(content)
	for atype in e.findall('.//node'):
		nodes.append(atype.get('TEXT'))

with open('mm.json', 'w') as outfile:
  json.dump(nodes, outfile)
 
#print json.dumps(nodes)
