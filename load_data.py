
from pymongo import MongoClient
import glob
import json
import time

client = MongoClient('localhost', 27017)
db = client['election']
collection = db['vote']


vote_file_list = glob.glob("data/*.txt")
for vote_file in vote_file_list:
	with open(vote_file) as f:
		lines = f.readlines()
		for i, line in enumerate(lines):
			line = line.split(";")
			data = {}
			data["date"] = line[0].strip()
			data["city"] = line[1].strip()
			data["vote"] = line[2].strip()
			collection.insert(data)
			if (i%20 == 0):
				time.sleep(5)

#candidate = "Clinton"
#number_vote_candidate = collection.find({"vote": candidate}).count()
#print(number_vote_candidate)



