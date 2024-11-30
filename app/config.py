import os
from dotenv import load_dotenv

load_dotenv()


MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGODB_URI = os.getenv("MONGODB_URI")
