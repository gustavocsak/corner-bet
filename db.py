import pymongo
import os
from pymongo import MongoClient 
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

cluster = MongoClient(f'mongodb+srv://{DB_USER}:{DB_PASS}@cluster0.5gryi.mongodb.net/Matches?retryWrites=true&w=majority')

db = cluster["Matches"]
predictions = db["predictions"]
results = db["results"]

