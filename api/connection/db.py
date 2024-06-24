# pip install Flask
# pip install Flask-Cors
# pip install pymongo
# db.py
from pymongo import MongoClient


def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['dockwitcher']
    return db


def get_collection(collection_name):
    db = get_db()
    return db[collection_name]
