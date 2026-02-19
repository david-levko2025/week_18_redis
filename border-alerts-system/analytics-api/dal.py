from mongo_connection import MongoConnection as mongo,settings


def alerts_by_border_and_priority():
    mongo_coll = mongo.get_collection(self=)
    query = mongo_coll.find({},{"border":1,"_id":0})
    return query
def top_urgent_zones():
    mongo_coll = mongo.get_collection(self=)
    query = mongo_coll.find({},{"zone":1,"_id":0})
    return query


def distance_distribution():
    mongo_coll = mongo.get_collection(self=)
    query = mongo_coll.find({})
    return query


def low_visibility_high_activity():
    mongo_coll = mongo.get_collection(self=)
    query = mongo_coll.find({},{"border":1,"_id":0})
    return query


def hot_zones():
    mongo_coll = mongo.get_collection(self=)
    query = mongo_coll.find({},{"border":1,"_id":0})
    return query