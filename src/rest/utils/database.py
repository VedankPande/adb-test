import os

from pymongo import MongoClient


def get_db_connection():
    """
    Returns MongoDB database connection object
    """
    mongo_uri = 'mongodb://' + \
        os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
    db = MongoClient(mongo_uri)['adb']

    return db
