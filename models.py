from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime, timezone

load_dotenv()

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

app = Flask(__name__)

client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.yoczwia.mongodb.net/newterrab?retryWrites=true&w=majority&appName=Cluster0")
db = client['newterrab']

mongo = PyMongo(app)

# Sample data structure for categories
categories = [
    {"name": "Food Crops"},
    {"name": "Cash Crops"},
    {"name": "Mammals"},
    {"name": "Birds"},
    {"name": "Reptiles"},
    {"name": "Fish"},
    {"name": "Crustaceans"}
]

# Insert sample categories if not present
if mongo.db.categories.count_documents({}) == 0:
    mongo.db.categories.insert_many(categories)

# Sample data structure for products
products = [
    {
        "name": "Organic Tomatoes",
        "description": "Fresh organic tomatoes",
        "price": 5.99,
        "image": "/static/images/tomatoes.jpg",
        "category": "Food Crops",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 4
    },
    {
        "name": "Free-Range Chicken",
        "description": "Healthy free-range chicken",
        "price": 12.50,
        "image": "/static/images/chicken.jpg",
        "category": "Mammals",
        "is_featured": True,
        "created_at":  datetime.now(timezone.utc),
        "rating": 5
    },
    {
        "name": "Tilapia Fish",
        "description": "Fresh tilapia fish",
        "price": 8.75,
        "image": "/static/images/fish.jpg",
        "category": "Fish",
        "is_featured": False,
        "created_at": datetime.now(timezone.utc),
        "rating": 3
    }
]

# Insert sample products if not present
if mongo.db.products.count_documents({}) == 0:
    mongo.db.products.insert_many(products)