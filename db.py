import pymongo
from pymongo import MongoClient 

cluster = MongoClient("mongodb+srv://gustavocs:admin@cluster0.5gryi.mongodb.net/Matches?retryWrites=true&w=majority")

db = cluster["Matches"]
collection = db["test"]

