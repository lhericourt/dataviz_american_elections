from flask import Flask, request, render_template, url_for, Blueprint, jsonify
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import chartkick
import pandas  as pd
import os
from indicators import *
import locale

DB = "election"
STATE = "state"
RESULT_BY_STATE = "result_by_state"

# Connection to MongoDB
client = MongoClient('localhost', 27017)
db = client[DB]
collection_state = db[STATE]
collection_result_by_state = db[RESULT_BY_STATE]

app = Flask(__name__)

data_victory = [
    ["mo", "Clinton"],
    ["ks", "Trump"],
    ["or", "Trump"]
]


nb_votes = [
    ["mo", "Clinton", 98726],
    ["mo", "Trump", 62524],
    ["mo", "Dupont", 14253],
    ["ks", "Clinton", 52423],
    ["ks", "Trump", 52441],
    ["ks", "Dupont", 1526],
    ["or", "Clinton", 938735],
    ["or", "Trump", 162552],
    ["or", "Dupont", 14253],
]


@app.route('/background_process_indicators')
def background_process_indicators():
    try:

        print('====== in background_process_indicators! =====')
        #candidate = request.args.get('candidate', "", type=str)

        nb_of_votes, nb_of_suffrages, nb_Abstention, nb_of_votes_republicains, nb_of_votes_democrates, nb_of_votes_autres = get_indicators(collection_result_by_state,collection_state)

        print ("votants = "+str(nb_of_votes)+" sufrages = "+str(nb_of_suffrages)+" Abstention = "+str(nb_Abstention)+" republicains = "+str(nb_of_votes_republicains)+" democrates = "+str(nb_of_votes_democrates)+" autres = "+str(nb_of_votes_autres))

        unite = 1000000 # millier
        nb_of_votes = (format(nb_of_votes / unite, ",f"))[:5]
        nb_of_suffrages = (format(nb_of_suffrages / unite, ",f"))[:5]
        nb_Abstention = (format(nb_Abstention / unite, ",f"))[:5]
        nb_of_votes_republicains = (format(nb_of_votes_republicains / unite, ",f"))[:5]
        nb_of_votes_democrates = (format(nb_of_votes_democrates / unite, ",f"))[:5]
        nb_of_votes_autres = (format(nb_of_votes_autres / unite, ",f"))[:5]

        return jsonify(nb_of_votes=str(nb_of_votes),
                       nb_of_suffrages=str(nb_of_suffrages),
                       nb_Abstention=str(nb_Abstention),
                       nb_of_votes_republicains=str(nb_of_votes_republicains),
                       nb_of_votes_democrates = str(nb_of_votes_democrates),
                       nb_of_votes_autres = str(nb_of_votes_autres)
                       ,
                       )
    except Exception as e:
        print(e)
        return str(e)

index_victory = 0
@app.route('/background_process_map')
def background_process_map():
    global index_victory
    if index_victory < 4:
        index_victory += 1
    try:
        print('===== in background_process_map! =====')
        #return jsonify(data_victory_process=data_victory[0:index_victory])
        return jsonify(data_victory_process="test_from_python")

    except Exception as e:
        return str(e)

@app.route('/')
def index():
    nb_of_votes, nb_of_suffrages, nb_Abstention, nb_of_votes_republicains, nb_of_votes_democrates, nb_of_votes_autres = get_indicators(collection_result_by_state,collection_state)

    # unite = 1000000 # millier
    # nb_of_votes = (format(nb_of_votes / unite, ",f"))[:5]
    # nb_of_suffrages = (format(nb_of_suffrages / unite, ",f"))[:5]
    # nb_Abstention = (format(nb_Abstention / unite, ",f"))[:5]
    # nb_of_votes_republicains = (format(nb_of_votes_republicains / unite, ",f"))[:5]
    # nb_of_votes_democrates = (format(nb_of_votes_democrates / unite, ",f"))[:5]
    # nb_of_votes_autres = (format(nb_of_votes_autres / unite, ",f"))[:5]

    return render_template('index.html',
                           data_victory=data_victory,
                           # nb_of_votes=str(nb_of_votes),
                           # nb_of_suffrages=str(nb_of_suffrages),
                           # nb_Abstention=str(nb_Abstention),
                           # nb_of_votes_republicains=str(nb_of_votes_republicains),
                           # nb_of_votes_democrates = str(nb_of_votes_democrates),
                           # nb_of_votes_autres = str(nb_of_votes_autres)
                           )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)

