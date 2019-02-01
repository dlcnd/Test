import json
from pprint import pprint

with open("output.json") as f:
	data = json.load(f)

print data["streams"][0]["width"]


'''
file structure
Ex)
"streams":[
	{
		"index": 0,
		"level": 31,
		"width": 1280
	}
]
print data.keys() // print keys of dictionary

print(data["streams"]) //print data of streams key

for i in data[streams]:
	print i
'''
