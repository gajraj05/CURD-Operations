import pymongo
from pymongo import MongoClient

url = 'mongodb://localhost:27017/'
client = MongoClient(url)

database = client['mydatabase']