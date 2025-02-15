from flask import Blueprint, request, redirect, url_for, flash, session, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from db.users import create_user, find_user_by_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if find_user_by_email(email):
        flash("Email already exists. Please log in.", "error")
        return redirect(url_for('auth.login'))

    hashed_password = generate_password_hash(password)
    user_id = create_user(username, email, hashed_password)

    flash("Registration successful! Please log in.", "success")
    return redirect(url_for('auth.login'))


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = find_user_by_email(email)

    if user and 'password_hash' in user and check_password_hash(user['password_hash'], password):
        session['user_id'] = str(user['_id'])  # Store user ID in session
        session['username'] = user['username']  # Store username in session
        flash("Login successful!")
        return redirect(url_for('products.show_products'))
    else:
        flash("Invalid credentials.")
        return redirect(url_for('auth.login'))



@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('auth.login'))
