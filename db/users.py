from flask import Blueprint, request, redirect, url_for, flash, render_template, session 
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.yoczwia.mongodb.net/newterrab?retryWrites=true&w=majority&appName=Cluster0")
db = client['newterrab']


users_bp = Blueprint('register', __name__)

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        flash('Registration successful! Please log in.')
        return redirect(url_for('users.login'))
    return render_template("register.html")

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Fetch user from database (placeholder logic)
        if email == "user@example.com" and check_password_hash("hashed_password", password):
            session['user_id'] = 1  # Simulate logged-in user
            flash('Login successful!')
            return redirect(url_for('products.show_products'))
        else:
            flash('Invalid email or password.')
    return render_template('login.html')

@users_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.')
    return redirect(url_for('products.show_products'))


# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)



users_collection = db['users']

def create_user(username, email, password_hash):
    user_data = {
        "username": username,
        "email": email,
        "password_hash": password_hash,
    }
    result = users_collection.insert_one(user_data)
    return result.inserted_id

def find_user_by_email(email):
    return users_collection.find_one({"email": email})