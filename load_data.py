
from pymongo import MongoClient
import glob
import json
import time
import re
from collections import Counter

DB = "election"

VOTE = "vote"
STATE = "state"
RESULT_BY_STATE = "result_by_state"


client = MongoClient('localhost', 27017)
db = client[DB]
collection_vote = db[VOTE]
collection_state = db[STATE]
collection_result_by_state = db[RESULT_BY_STATE]

basename = "data1"
vote_file_list = glob.glob(basename+"/*.txt")

minute = 1
while minute <= 60:
	if len(str(minute)) < 2:
		min_str = '0'+str(minute)
	else:
		min_str = str(minute)
	#print (min_str)
	res = [f for f in vote_file_list if re.search(re.escape(basename) + r'\\\d{4}-\d{2}-\d{2}-\d{2}-'+re.escape(min_str)+r'_\w*.txt', f)]

	for vote_file in res:
		print ("File: "+vote_file)
		with open(vote_file) as f:
			lines = f.readlines()
			nb_electors = 0
			#cnt = Counter()
			for i, line in enumerate(lines):
				line = line.split(",")
				#cnt.update([line[2].strip()])
				data_result_by_state = {}
				data_result_by_state["candidate"] = line[2].strip()
				data_result_by_state["state_name"] = line[1].strip()
				data_result_by_state["nb_of_votes"] = line[3].strip()
				#print(data_result_by_state)
				collection_result_by_state.insert(data_result_by_state)
	time.sleep(60)
	minute = minute + 1
	if (minute == 60):
		break





# result_by_state_nb_of_votes = "nb_of_votes"
# result_by_state_candidate = "candidate"
# result_by_state_name = "state_name"
# state_nb_subscriptors  = "nb_subscriptors"


# result_by_state = collection_result_by_state.find({},{result_by_state_nb_of_votes:"1","_id":"0",result_by_state_candidate:"1", result_by_state_name:"1"})


# nb_of_votes = 0
# for result in result_by_state:

# 	state = collection_state.find_one({result_by_state_name:result[result_by_state_name]},{"nb_electors":"1","_id":"0","nb_subscriptors":"1"})
# 	nb_of_votes = nb_of_votes + int(result[result_by_state_nb_of_votes])

# 	#print(state)
# 	print(result[result_by_state_nb_of_votes], result[result_by_state_candidate], result[result_by_state_name], state[state_nb_subscriptors])


# print ("somme "+str(nb_of_votes))

# print (format(6270255, ",d"))
# val = 6270255 /1000000
# print ((format(val, ",f"))[:5])
# val1 = 200000 /1000000
# print ((format(val1, ",f"))[:5])

