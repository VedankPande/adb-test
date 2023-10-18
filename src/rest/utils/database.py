import sys
import os
import logging
from abc import ABC, abstractmethod

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError

class DatabaseInterface(ABC):
    """
    Abstract high level database interface
    """
    
    @abstractmethod
    def disconnect(self):
        pass

class NoSQLDatabaseInterface(DatabaseInterface):
    """
    Abstract NoSQL Database interface to be used by concrete 
    classes
    """
    
    @abstractmethod
    def get_collection(self, collection_name: str):
        pass

class MongoDBDatabase(NoSQLDatabaseInterface):
    """
    Database class to store client connections and return specified collection(s)
    """

    def __init__(self, url: str, db_name: str):
        try:
            self.client = MongoClient(url)
            self.database = self.client[db_name]
        except ConnectionFailure as e:
            logging.error(f"Error while connecting to MongoDB: {e}")
        except PyMongoError as e:
            logging.error(f"PyMongo error: {e}")
        
    def get_collection(self, collection_name: str):
        return self.database[collection_name]

    def disconnect(self):
        self.client.close()
