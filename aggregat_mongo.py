from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'projet'
COLLECTION_NAME = 'result'

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DBS_NAME][COLLECTION_NAME]
pipeline = [{"$match": {"$or": [{"candidat": "Trump"}, {"candidat": "Clinton"}]}},
            {"$group": {"_id": {"etat": "$etat", "candidat": "$candidat"}, "count": {"$sum": 1}}},
            {"$sort": {"_id": -1}}]

print(list(collection.aggregate(pipeline)))
