# db/products.py
from pymongo import ReturnDocument
from bson.objectid import ObjectId
from db.dbconnection import db

products_collection = db['products']

def create_product(name, price, description, image, category, gender=None, color=None):
    product_data = {
        "name": name,
        "price": price,
        "description": description,
        "image": image,
        "category": category,
        "gender": gender,
        "color": color,
    }
    result = products_collection.insert_one(product_data)
    return result.inserted_id

def get_all_products():
    return list(products_collection.find())

def get_product_by_name(name):
    return products_collection.find_one({"name": name})

def update_product(name, new_name, price, description, image, category, gender=None, color=None):
    query = {"name": name}
    new_values = {
        "$set": {
            "name": new_name,
            "price": price,
            "description": description,
            "image": image,
            "category": category,
            "gender": gender,
            "color": color
        }
    }
    return products_collection.update_one(query, new_values)

def delete_product(name):
    return products_collection.delete_one({"name": name}).deleted_count

