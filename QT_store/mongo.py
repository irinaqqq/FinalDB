# myapp/mongo.py
from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["qt2"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()
