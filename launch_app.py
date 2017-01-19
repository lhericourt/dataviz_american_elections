from flask import Flask, request, render_template, url_for, Blueprint, jsonify
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import chartkick
import pandas  as pd
import os

# Connection to MongoDB
client = MongoClient('localhost', 27017)
db = client['election']
collection = db['vote']

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
        print('in background_process_indicators!')
        candidate = request.args.get('candidate', "", type=str)

        #number_vote_candidate_clinton = collection.find({"vote": "Clinton"}).count()
        #number_vote_candidate_trump = collection.find({"vote": "Trump"}).count()
        return jsonify(number_vote_candidate_clinton=str("toto"),
                       number_vote_candidate_trump=str("test"))
    except Exception as e:
        return str(e)

index_victory = 0
@app.route('/background_process_map')
def background_process_map():
    global index_victory
    if index_victory < 4:
        index_victory += 1
    try:
        print('in background_process_map!')
        return jsonify(data_victory_process=data_victory[0:index_victory])
        #return jsonify(data_victory_process="test_from_python")

    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html', data_victory=data_victory, nb_votes=nb_votes)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)

