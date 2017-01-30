from flask import Flask, request, render_template, url_for, Blueprint, jsonify
from pymongo import MongoClient, errors
import json
from bson import json_util
from bson.json_util import dumps

import pandas  as pd
import numpy as np
import os
from indicators import *
import locale
from numpy.random import randint

import time
from indicators import *
import locale
import logging, sys

logging.basicConfig(stream=sys.stderr)

VOTE_REPUBLICAIN = "Trump"
VOTE_DEMOCRATE = "Clinton"

# Connection to MongoDB
client = MongoClient("localhost", 27017)
#client = MongoClient('mongodb://sfr:sfr@172.31.19.90,172.31.34.107,172.31.21.107/election?replicaset=rs0', 27017)
db = client['election']
collection_state = db['state']
collection_result = db['result_by_state']

# Chargement de la matrice de prédiction
prediction_matrix = pd.read_csv("data/matrix_predict.csv")
#prediction_matrix = pd.read_csv("projet/gentelella/production/data/matrix_predict.csv")
prediction_matrix["real"] = 0
prediction_matrix['state_code'] = prediction_matrix['state_code'].str.lower()


# Fonction qui retourne toutes les données de résultat agrégées
def get_all_data():
    complete_result = ""
    for i in range(5):
        try:
            result = pd.DataFrame(list(collection_result.find()))
            state = pd.DataFrame(list(collection_state.find()))
            state['state_code'] = state['state_code'].str.lower()
            complete_result = pd.merge(result, state, on='state_name')
            break
        except errors.AutoReconnect:
            time.sleep(pow(2, i))

    return complete_result

# Fonction qui retourne pour chaque état les résultats
def get_victory_by_state (complete_result):
    data_victory = ""
    for i in range(5):
        try:
            idx_winner = complete_result.groupby(['state_code'])['nb_of_vote'].transform(max) == complete_result['nb_of_vote']
            data_victory = complete_result[idx_winner][["state_code", "candidate"]].as_matrix()
            data_victory = data_victory.tolist()
            break
        except errors.AutoReconnect:
                time.sleep(pow(2, i))

    return data_victory

# Fonction qui retourne le nombre de votes par etat et par candidat
def get_nb_of_votes (complete_result):
    nb_votes = complete_result[["state_code", "candidate", "nb_of_vote"]].as_matrix()
    nb_votes = nb_votes.tolist()
    return nb_votes

def get_estimated_electors(data_victory):
    data_victory_df = pd.DataFrame(data_victory, columns = ["state_code", "winner"])
    compute_victory_df = pd.merge(prediction_matrix, data_victory_df, how='left', on="state_code")
    trump_real_victory = compute_victory_df[compute_victory_df["winner"] == "Trump"]
    clinton_real_victory = compute_victory_df[compute_victory_df["winner"] == "Clinton"]
    trump_assumed_victory = compute_victory_df[(compute_victory_df["winner"].isnull()) & (compute_victory_df["forcast"] == 1)]
    clinton_assumed_victory = compute_victory_df[(compute_victory_df["winner"].isnull()) & (compute_victory_df["forcast"] == -1)]
    trump_nb_electors =  trump_assumed_victory["nb_electors"].sum() + trump_real_victory["nb_electors"].sum()
    clinton_nb_electors =  clinton_assumed_victory["nb_electors"].sum() + clinton_real_victory["nb_electors"].sum()
    return trump_nb_electors, clinton_nb_electors


app = Flask(__name__)


@app.route('/background_process_indicators')
def background_process_indicators():
    try:

        print('====== in background_process_indicators! =====')
        #trump_big_elector_timeline = request.args.getlist('trump_big_elector_timeline[]')
        #print(trump_big_elector_timeline)
        #clinton_big_elector_timeline = request.args.get('clinton_big_elector_timeline', "", type=list)
        #autres_big_elector_timeline = request.args.get('autres_big_elector_timeline', "", type=list)



        nb_of_votes, nb_of_suffrages, nb_Abstention, nb_of_votes_republicains, nb_of_votes_democrates, nb_of_votes_autres, big_elector = get_indicators(collection_result,collection_state)

        #print ("votants = "+str(nb_of_votes)+" sufrages = "+str(nb_of_suffrages)+" Abstention = "+str(nb_Abstention)+" republicains = "+str(nb_of_votes_republicains)+" democrates = "+str(nb_of_votes_democrates)+" autres = "+str(nb_of_votes_autres))

        # trump_big_elector_timeline = list(randint(0, 9, size=7))
        # clinton_big_elector_timeline = list(randint(0, 9, size=7))
        # autres_big_elector_timeline = list(randint(0, 9, size=7))

        trump_big_elector_timeline = 0
        clinton_big_elector_timeline = 0
        autres_big_elector_timeline = 0

        for k,v in big_elector.items():
            if (k == VOTE_REPUBLICAIN):
                trump_big_elector_timeline = v
            elif (k == VOTE_DEMOCRATE):
                clinton_big_elector_timeline = v
            else:
                autres_big_elector_timeline = v


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
                       nb_of_votes_autres = str(nb_of_votes_autres),
                       #big_elector = big_elector,
                        trump_big_elector_timeline  = str(trump_big_elector_timeline),
                        clinton_big_elector_timeline = str(clinton_big_elector_timeline),
                        autres_big_elector_timeline = str(autres_big_elector_timeline)
                       )
    except Exception as e:
        print(e)
        return str(e)


@app.route('/background_process_map')
def background_process_map():

    #print('====== in background_process_map! =====')

    complete_result = get_all_data()
    data_victory = get_victory_by_state(complete_result)
    nb_votes = get_nb_of_votes(complete_result)
    try:
        return jsonify(data_victory_process=data_victory, nb_votes_process=nb_votes)
    except Exception as e:
        return str(e)

@app.route('/background_process_histo')
def background_process_histo():

    #print('====== in background_process_histo! =====')

    complete_result = get_all_data()
    data_victory = get_victory_by_state(complete_result)

    trump_nb_electors, clinton_nb_electors = get_estimated_electors(data_victory)

    try:
        return jsonify(trump_nb_electors_process=str(trump_nb_electors), clinton_nb_electors_process=str(clinton_nb_electors))
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    nb_of_votes, nb_of_suffrages, nb_Abstention, nb_of_votes_republicains, nb_of_votes_democrates, nb_of_votes_autres, big_elector = get_indicators(collection_result,collection_state)

    # trump_big_elector_timeline = list(randint(0, 9, size=7))
    # clinton_big_elector_timeline = list(randint(0, 9, size=7))
    # autres_big_elector_timeline = list(randint(0, 9, size=7))

    trump_big_elector_timeline = 0
    clinton_big_elector_timeline = 0
    autres_big_elector_timeline = 0

    for k,v in big_elector.items():
        if (k == VOTE_REPUBLICAIN):
            trump_big_elector_timeline = v
        elif (k == VOTE_DEMOCRATE):
            clinton_big_elector_timeline = v
        else:
            autres_big_elector_timeline = v

    unite = 1000000 # millier
    nb_of_votes = (format(nb_of_votes / unite, ",f"))[:5]
    nb_of_suffrages = (format(nb_of_suffrages / unite, ",f"))[:5]
    nb_Abstention = (format(nb_Abstention / unite, ",f"))[:5]
    nb_of_votes_republicains = (format(nb_of_votes_republicains / unite, ",f"))[:5]
    nb_of_votes_democrates = (format(nb_of_votes_democrates / unite, ",f"))[:5]
    nb_of_votes_autres = (format(nb_of_votes_autres / unite, ",f"))[:5]

    return render_template('index.html',
                           nb_of_votes=str(nb_of_votes),
                           nb_of_suffrages=str(nb_of_suffrages),
                           nb_Abstention=str(nb_Abstention),
                           nb_of_votes_republicains=str(nb_of_votes_republicains),
                           nb_of_votes_democrates = str(nb_of_votes_democrates),
                           nb_of_votes_autres = str(nb_of_votes_autres),
                           #big_elector = big_elector
                           trump_big_elector_timeline  = str(trump_big_elector_timeline),
                           clinton_big_elector_timeline = str(clinton_big_elector_timeline),
                           autres_big_elector_timeline = str(autres_big_elector_timeline)
                           )



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)

