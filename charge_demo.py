# coding: utf-8

import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/')
sys.path.append("/Users/lolo/3.5.1 - Pour Big Data/lib/python3.5/site-packages/")

from pymongo import MongoClient, errors
import glob
import json
import time
import re
from collections import Counter

DB = "election"

VOTE = "vote"
STATE = "state"
RESULT_BY_STATE = "result_by_state"


#client = MongoClient('mongodb://sfr:sfr@172.31.19.90,172.31.34.107,172.31.21.107/election?replicaset=rs0', 27017)
client = MongoClient("localhost", 27017)

db = client[DB]
collection_vote = db[VOTE]
collection_state = db[STATE]
collection_result_by_state = db[RESULT_BY_STATE]

#basename = "/home/ubuntu/data/etats_usa"
basename = "/Users/lolo/Développement/Projet NoSQL/data/etats_usa"

vote_file_list = glob.glob(basename+"/*.txt")

minute = 11
while minute <= 60:
        if len(str(minute)) < 2:
                min_str = '0'+str(minute)
        else:
                min_str = str(minute)
        print (min_str)
        res = [f for f in vote_file_list if re.search(re.escape(basename) + r'/\d{4}-\d{2}-\d{2}-\d{2}-'+re.escape(min_str)+r'_\w*.txt', f)]

        for vote_file in res:
                print ("File: "+vote_file)
                with open(vote_file) as f:
                        lines = f.readlines()
                        nb_electors = 0
                        #cnt = Counter()
                        for i, line in enumerate(lines):
                                if (i != 0):
                                        line = line.split(",")
                                        #cnt.update([line[2].strip()])
                                        data_result_by_state = {}
                                        data_result_by_state["candidate"] = line[2].strip()
                                        data_result_by_state["state_name"] = line[1].strip()
                                        data_result_by_state["nb_of_vote"] = int(line[3].strip())
                                        #print(data_result_by_state)
                                        for i in range(5):
                                            try:
                                                collection_result_by_state.insert(data_result_by_state)
                                                break
                                            except errors.AutoReconnect:
                                                time.sleep(pow(2, i))
        time.sleep(5)
        minute = minute + 1
        # if (minute == 60):
        #       break


