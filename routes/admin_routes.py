from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, session
from db.products import create_product, update_product, delete_product, get_all_products, get_product_by_name
import os
from .decorators import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/products')
@admin_required
def admin_products():
    products = get_all_products()
    return render_template('admin_products.html', products=products)

@admin_bp.route('/products/add', methods=['GET', 'POST'])
@admin_required
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        category = request.form.get('category')
        # gender = request.form.getlist('gender')
        # color = request.form.getlist('color')
        if category in ['mammals', 'birds', 'reptiles']:
            gender = request.form.get('gender')
            color = request.form.get('color')
        else:
            gender = None
            color = None
        # Handle image upload
        image = request.files['image']
        if image:
            filename = image.filename
            upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)  # Ensure the upload folder exists
            image_path = os.path.join(upload_folder, filename)
            image.save(image_path)
            image_url = f"/static/uploads/{filename}"
        else:
            image_url = None

        create_product(name, price, description, image_url, category, gender, color)
        flash('Product added successfully!')
        return redirect(url_for('admin.admin_products'))
    
    return render_template('admin_add_product.html')

@admin_bp.route('/products/update/<string:name>', methods=['GET', 'POST'])
@admin_required
def update_product_route(name):
    product = get_product_by_name(name)  # Implement this function in db/products.py
    if not product:
        flash('Product not found!')
        return redirect(url_for('admin.admin_products'))

    if request.method == 'POST':
        new_name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        category = request.form.get('category')
        # gender = request.form.getlist('gender')
        # color = request.form.getlist('color')

        # Handle gender and color only for mammals, birds, and reptiles
        if category in ['mammals', 'birds', 'reptiles']:
            gender = request.form.get('gender')
            color = request.form.get('color')
        else:
            gender = None
            color = None

        # Handle image upload
        image = request.files['image']
        if image:
            filename = image.filename
            upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)  # Ensure the upload folder exists
            image_path = os.path.join(upload_folder, filename)
            image.save(image_path)
            image_url = f"/static/uploads/{filename}"
        else:
            image_url = product['image']  # Keep the existing image if no new image is uploaded

        update_product(name, new_name, price, description, image_url, category, gender, color)
        flash('Product updated successfully!')
        return redirect(url_for('admin.admin_products'))
    
    return render_template('admin_update_product.html', product=product)

@admin_bp.route('/products/delete/<string:name>', methods=['POST'])
@admin_required
def delete_product_route(name):
    delete_product(name)
    flash('Product deleted successfully!')
    return redirect(url_for('admin.admin_products'))

# @admin_bp.route("/dashboard")
# @admin_required
# def admin_dashboard():
#     return redirect(url_for('admin.admin_products'))



@admin_bp.route("/dashboard")
@admin_required
def admin_dashboard():
    if not session.get("is_admin"):
        flash("Unauthorized access!", "danger")
        return redirect(url_for("home.home"))
    return redirect(url_for('admin.admin_products'))
