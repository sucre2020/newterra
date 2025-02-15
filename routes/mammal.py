from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db.products import get_all_products, find_product_by_name

mammal_bp = Blueprint('mammal', __name__)

@mammal_bp.route('/mammal')
def mammal():
    return render_template('mammal.html')