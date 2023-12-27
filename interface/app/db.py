import pandas as pd
from pymongo import MongoClient
from env import MONGO_URL, DATABASE_NAME

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]
collection = db["tatoeba"]
data = pd.DataFrame(list(collection.find()))


def get_data():
    return data


def get_collection():
    return collection
