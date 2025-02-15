from flask import Blueprint, render_template, request
from db.dbconnection import db

collection = db["products"]

search_bp = Blueprint('search', __name__)

@search_bp.route('/search')
def search():
    query = request.args.get('query')
    if query:
        # MongoDB case-insensitive regex search
        results = collection.find({"name": {"$regex": query, "$options": "i"}})
    else:
        results = []
    return render_template('search_results.html', results=results)