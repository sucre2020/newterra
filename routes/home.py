from flask import Blueprint, render_template
from db.dbconnection import db

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    featured_products = list(db.products.find({"is_featured": True}))
    latest_products = list(db.products.find().sort("created_at", -1).limit(8))

    return render_template('home.html', featured_products=featured_products, latest_products=latest_products)


