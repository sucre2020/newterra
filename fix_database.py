from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.yoczwia.mongodb.net/newterrab?retryWrites=true&w=majority&appName=Cluster0")
db = client['newterrab']

# Set default rating for products missing the rating field
db.products.update_many({"rating": {"$exists": False}}, {"$set": {"rating": 0}})

print("Database updated successfully!")
