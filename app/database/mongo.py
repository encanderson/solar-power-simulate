from pymongo import MongoClient
from app.config import settings


class Database:
    URI = settings.MONGO_DB_URL
    db = None

    @staticmethod
    def initialize():
        client = MongoClient(Database.URI)
        Database.db = client['projects']

    @staticmethod
    def insert(collection, data):
        return Database.db[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.db[collection].find(query)

    @staticmethod
    def find_one(collection, query, params):
        return Database.db[collection].find_one(query, params)

    @staticmethod
    def update(collection, query, update):
        return Database.db[collection].update_one(query, update, upsert=True)

    @staticmethod
    def delete(collection, query):
        return Database.db[collection].delete_one(query)


db = Database
db.initialize()
