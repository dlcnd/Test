from pymongo import MongoClient
import datetime

client = MongoClient("10.10.10.226", 27017)
db = client.projects #db name
project = "circle" # collection
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

"""
#data insert
item = {"name":"BAR_0010",
		"text":"fire and sky artwork",
		"tags":["fire","sky"],
		"date":date,
}
db[project].insert_one(item)
"""
"""
#data get
for doc in db[project].find():
	print(doc.get("name",""))
	print(doc.get("text",""))
	tags = doc.get("tags",[])
	for tag in tags:
		print("\t"+tag)
"""
"""
#data update
item = db[project].find_one({"name":"BAR_0010"})
item["date"]=date
item["text"]="new text"
db[project].update_one({"name":"BAR_0010"},{"$set":item})
"""
#date delete
result = db[project].delete_many({"name":"BAR_0010"})

