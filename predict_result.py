from pymongo import MongoClient
#from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

# Connection to MongoDB
client = MongoClient("localhost", 27017)
db = client['election']
collection_past_result = db['past_result']
collection_state = db['state']

def return_winner(x):
    if x > 0:
        return 1
    else:
        return -1

past_result = pd.DataFrame(list(collection_past_result.find()))
state = pd.DataFrame(list(collection_state.find()))

past_result = past_result.set_index(["State"])

past_result = past_result.drop(["_id"], axis=1)

past_result_without_2016 = past_result.replace(['SR', "I", "AI", "PR", ""], [0, 0, 0, 0, 0])

# 1 pour républicains et -1 pour démocrates
past_result_without_2016 = past_result_without_2016.replace(['R', 'D'], [1, -1])
past_result_without_2016 = past_result_without_2016.drop(["2016"], axis=1)


# Pondération par 2 des 50 dernières années
past_result_without_2016[past_result_without_2016.columns[-15:-5]] = past_result_without_2016[past_result_without_2016.columns[-15:-5]] * 2

# Pondération par 3 des 20 dernières années
past_result_without_2016[past_result_without_2016.columns[-5:]] = past_result_without_2016[past_result_without_2016.columns[-5:]] * 3

past_result_without_2016["sum"] = past_result_without_2016.sum(axis=1)

past_result_without_2016["forcast"] = past_result_without_2016.apply(axis=1, func= lambda x:return_winner(x["sum"]))

past_result_without_2016["real"] = past_result["2016"].replace(['R', 'D'], [1, -1])
past_result_without_2016["error"] = past_result_without_2016["real"] - past_result_without_2016["forcast"]


print(past_result_without_2016[past_result_without_2016["error"] != 0].shape[0])
past_result_without_2016['state_name'] = past_result_without_2016.index
matrix_predict = pd.merge(past_result_without_2016, state, on='state_name')
matrix_predict = matrix_predict[["state_name", "state_code", "nb_electors","forcast"]]

matrix_predict.to_csv('data/matrix_predict.csv')


print(matrix_predict)





