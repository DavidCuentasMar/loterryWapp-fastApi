import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", None)
conn = MongoClient(mongo_uri)