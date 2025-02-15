from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime, timezone
from db.dbconnection import db  # Importing existing db connection

# load_dotenv()

# app = Flask(__name__)

# db_username = os.getenv("DB_USERNAME")
# db_password = os.getenv("DB_PASSWORD")

# client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.yoczwia.mongodb.net/newterrab?retryWrites=true&w=majority&appName=Cluster0")
# db = client['newterrab']


# messages_collection = db.messages
# print("Message collection added")

# Reference MongoDB collections
categories_collection = db["categories"]
products_collection = db["products"]

# Sample categories
categories = [
    {"name": "Food Crops"},
    {"name": "Cash Crops"},
    {"name": "Mammals"},
    {"name": "Birds"},
    {"name": "Reptiles"},
    {"name": "Fish"},
    {"name": "Crustaceans"},
    {"name": "Insects"}
]

# Insert sample categories if not present
if categories_collection.count_documents({}) == 0:
    categories_collection.insert_many(categories)
    print("Sample categories added!")

# Sample products
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
        "gender_options": ["Male", "Female"],
        "color_options": ["Black", "White", "Brown"],
        "created_at": datetime.now(timezone.utc),
        "rating": 5
    },
    {
        "name": "Tilapia Fish",
        "description": "Fresh tilapia fish",
        "price": 8.75,
        "image": "/static/images/tilapiafish.jpg",
        "category": "Fish",
        "is_featured": False,
        "created_at": datetime.now(timezone.utc),
        "rating": 3
    },
    {
        "name": "Cat Fish",
        "description": "Fresh Cat fish",
        "price": 8.75,
        "image": "/static/images/catfish.jpg",
        "category": "Fish",
        "is_featured": False,
        "created_at": datetime.now(timezone.utc),
        "rating": 3
    },
    {
        "name": "Mackerel Fish",
        "description": "Mackerel fish",
        "price": 8.75,
        "image": "/static/images/mackerel.jpg",
        "category": "Fish",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 3
    },
    {
        "name": "Bees",
        "price": 20000,
        "description": "Healthy farm bees",
        "image": "/static/images/bees.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown", "White", "Black"],
        "category": "Insects",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 4
    },
    {
        "name": "Dry Grasshoppers",
        "price": 10000,
        "description": "Dry Grasshoppers",
        "image": "/static/images/drygrasshoppers.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown", "White", "Black"],
        "category": "Insects",
        "created_at": datetime.now(timezone.utc),
        "rating": 4
    },
    {
        "name": "Fresh Grasshoppers",
        "price": 5000,
        "description": "Fresh Grasshoppers",
        "image": "/static/images/grasshoppersfresh.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown", "White", "Black"],
        "category": "Insects"
    },
    {
        "name": "Bison",
        "price": 150000,
        "description": "Well-fed bison for farming/meat",
        "image": "/static/images/bison.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Mammals"
    },
    {
        "name": "Buffalo",
        "price": 200000,
        "description": "Healthy buffalo for meat/farming",
        "image": "/static/images/bufalo.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Brown", "White", "Black"],
        "category": "Mammals"
    },
    {
        "name": "Duck",
        "price": 40000,
        "description": "Farm-bred duck",
        "image": "/static/images/ducks.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Birds",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 4
    },
    {
        "name": "Geese",
        "price": 45000,
        "description": "Farm-bred geese",
        "image": "/static/images/geese.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Birds"
    },
    {
        "name": "Horses",
        "price": 400000,
        "description": "Farm-bred horse",
        "image": "/static/images/horses.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Mammals"
    },
    {
        "name": "Guinea Pig",
        "price": 60000,
        "description": "Farm-bred guinea pig",
        "image": "/static/images/guinea_pigs.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Mammals",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 4,
    },
    {
        "name": "Donkey",
        "price": 175000,
        "description": "Donkey for farming/etc",
        "image": "/static/images/donkey.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Mammals"
    },
    {
        "name": "Crabs",
        "price": 17000,
        "description": "Crabs",
        "image": "/static/images/crabs.jpeg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Crustaceans"
    },
    {
        "name": "Lobsters",
        "price": 17000,
        "description": "Fresh Lobsters",
        "image": "/static/images/lobsters.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Crustaceans"
    },
    {
        "name": "Fresh Prawns",
        "price": 15000,
        "description": "Fresh Prawns",
        "image": "/static/images/freshprawns.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Crustaceans"
    },
    {
        "name": "Dry Prawns",
        "price": 17000,
        "description": "Dry Prawns",
        "image": "/static/images/dryprawns.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Crustaceans"
    },
    {
        "name": "Turtle",
        "price": 20000,
        "description": "Turtles",
        "image": "/static/images/turtles.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Reptiles"
    },
    {
        "name": "Crocodile",
        "price": 30000,
        "description": "Crocodiles",
        "image": "/static/images/crocodiles.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Reptiles"
    },
    {
        "name": "Alligator",
        "price": 40000,
        "description": "Alligators",
        "image": "/static/images/aligators.jpg",
        "gender_options": ["Male", "Female"],
        "color_options": ["Pink", "Brown", "Black"],
        "category": "Reptiles"
    },
    {
        "name": "Wheat",
        "price": 5000,
        "description": "High-quality wheat grains",
        "image": "/static/images/wheat.jpg",
        "category": "Food Crops"
    },
    {
        "name": "Rice",
        "price": 8000,
        "description": "Organic rice grains",
        "image": "/static/images/rice.jpg",
        "category": "Food Crops",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 4
    },
    {
        "name": "Coffee",
        "price": 12000,
        "description": "Premium coffee beans",
        "image": "/static/images/coffee.jpg",
        "category": "Cash Crops",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 4
    },
    {
        "name": "Cocoa",
        "price": 15000,
        "description": "High-quality cocoa beans",
        "image": "/static/images/cocoa.jpg",
        "category": "Cash Crops",
        "is_featured": True,
        "created_at": datetime.now(timezone.utc),
        "rating": 4
    }
]

# Insert sample products if not present
if products_collection.count_documents({}) == 0:
    products_collection.insert_many(products)
    print("Sample products added!")
else:
    print("Products already exist in the database.")
