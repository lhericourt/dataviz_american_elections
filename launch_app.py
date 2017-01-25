from flask import Flask, request, render_template, url_for, Blueprint, jsonify
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import pandas  as pd

# Connection to MongoDB
client = MongoClient("localhost", 27017)
db = client['election']
collection_state = db['state']
collection_result = db['result_by_state']

# Fonction qui retourne toutes les données de résultat agrégées
def get_all_data():
    result = pd.DataFrame(list(collection_result.find()))
    state = pd.DataFrame(list(collection_state.find()))
    state['state_code'] = state['state_code'].str.lower()
    complete_result = pd.merge(result, state, on='state_name')
    return complete_result

# Fonction qui retourne pour chaque état les résultats
def get_victory_by_state (complete_result):
    idx_winner = complete_result.groupby(['state_code'])['nb_of_vote'].transform(max) == complete_result['nb_of_vote']
    data_victory = complete_result[idx_winner][["state_code", "candidate"]].as_matrix()
    data_victory = data_victory.tolist()
    return data_victory

# Fonction qui retourne le nombre de votes par etat et par candidat
def get_nb_of_votes (complete_result):
    nb_votes = complete_result[["state_code", "candidate", "nb_of_vote"]].as_matrix()
    nb_votes = nb_votes.tolist()
    return nb_votes


app = Flask(__name__)


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
    complete_result = get_all_data()
    data_victory = get_victory_by_state(complete_result)
    nb_votes = get_nb_of_votes(complete_result)
    try:
        print('in background_process_map!')
        return jsonify(data_victory_process=data_victory[0:index_victory], nb_votes_process=nb_votes)
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    complete_result = get_all_data()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)

