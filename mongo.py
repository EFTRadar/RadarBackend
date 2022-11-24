from pymongo import MongoClient
import os
from dotenv import load_dotenv
import certifi

load_dotenv()

mongo = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
db = mongo["main"]
