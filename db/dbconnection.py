from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.yoczwia.mongodb.net/newterrab?retryWrites=true&w=majority&appName=Cluster0")
db = client['newterrab']


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



# users_collection = db['users']

# def create_user(name, email, password_hash):
#     user_data = {
#         "name": name,
#         "email": email,
#         "password_hash": password_hash,
#     }
#     result = users_collection.insert_one(user_data)
#     return result.inserted_id

# def find_user_by_email(email):
#     return users_collection.find_one({"email": email})