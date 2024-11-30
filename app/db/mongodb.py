import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()


mongo_user = os.getenv("MONGO_USER")
mongo_pass = os.getenv("MONGO_PASS")


mongodb_uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.jy7xm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(mongodb_uri)
db = client["student_management"]
collection = db["students"]
