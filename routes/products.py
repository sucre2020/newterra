from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from db.products import get_all_products, get_product_by_name

# Your route logic here
from db.dbconnection import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/category/<category>')
def category(category):
    products_collection = db["products"]
    products = list(products_collection.find({"category":category}))
    cart = session.get('cart', [])
    cart_item_count = sum(item['quantity'] for item in cart)
    return render_template("products.html", products=products, cart_item_count=cart_item_count, category=category)

@products_bp.route('/products')
def show_products():
    category = request.args.get('category')  # Get category from query params
    products_collection = db["products"]
    
    if category:
        products = list(products_collection.find({"category": category}))
    else:
        products = get_all_products()

    cart = session.get('cart', [])
    cart_item_count = sum(item['quantity'] for item in cart)
    return render_template('products.html', products=products, cart_item_count=cart_item_count)



@products_bp.route('/cart', methods=['POST'])
def cart():
    item_name = request.form.get("name")
    product = get_product_by_name(item_name)  # Fetch product from the database
    if product:
        item = {
            "name": product['name'],
            "price": product['price'],
            "gender": request.form.get("gender"),
            "color": request.form.get("color"),
            "quantity": 1
        }
        cart = session.setdefault('cart', [])
        existing_item = next(
            (i for i in cart if i['name'] == item['name'] and i['color'] == item['color'] and i['gender'] == item['gender']),
            None
        )
        if existing_item:
            existing_item['quantity'] += 1
            flash(f"Updated quantity of {item['name']} ({item['gender']}, {item['color']}) in cart.", "success")
        else:
            cart.append(item)
            flash(f"{item['name']} ({item['gender']}, {item['color']}) added to cart!", "success")
        session.modified = True
    else:
        flash(f"Product '{item_name}' not found.", "error")
    return redirect(url_for('products.show_products'))


@products_bp.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    print(cart)
    total_price = sum(float(item['price']) * int(item['quantity']) for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)




@products_bp.route('/update-cart/<name>', methods=['POST'])
def update_cart(name):
    cart = session.get('cart', [])
    new_quantity = int(request.form.get('quantity', 1))
    for item in cart:
        if item['name'] == name:
            item['quantity'] = new_quantity
            flash(f"Quantity updated for {name}.", "success")
            break
    else:
        flash(f"Item {name} not found in cart.", "error")

    session['cart'] = cart
    session.modified = True
    return redirect(url_for('products.view_cart'))


@products_bp.route('/remove-from-cart/<name>', methods=['POST'])
def remove_from_cart(name):
    cart = session.get('cart', [])
    initial_length = len(cart)
    cart = [item for item in cart if item['name'] != name]

    if len(cart) < initial_length:
        flash(f"{name} removed from cart.", "success")
    else:
        flash(f"{name} was not found in the cart.", "error")

    session['cart'] = cart
    session.modified = True
    return redirect(url_for('products.view_cart'))


@products_bp.route('/checkout', methods=['POST'])
def checkout():
    if not session.get('cart'):
        flash("Your cart is empty. Add items before checking out.", "error")
    else:
        session['cart'] = []
        session.modified = True
        flash("Checkout successful! Your cart has been cleared.", "success")
    return redirect(url_for('products.show_products'))

from bson.objectid import ObjectId  # Import ObjectId for MongoDB IDs

@products_bp.route('/cart/<product_id>')
def add_to_cart(product_id):
    products_collection = db["products"]
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    
    if not product:
        flash("Product not found!", "error")
        return redirect(url_for('products.show_products'))
    
    cart = session.get('cart', [])
    cart.append({
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "gender": request.form.get("gender"),
        "color": request.form.get("color"),
        "quantity": 1
    })
    session['cart'] = cart
    session.modified = True
    flash(f"{product['name']} added to cart!", "success")
    return redirect(url_for('products.view_cart'))

