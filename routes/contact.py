from flask import Flask, Blueprint, render_template, request, redirect, flash
from datetime import datetime, timezone
from db.dbconnection import db  # Import the correct db connection
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.yoczwia.mongodb.net/newterrab?retryWrites=true&w=majority&appName=Cluster0")
db = client['newterrab']

# Ensure messages_collection is properly set
messages_collection = db["messages"]

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])  # Allow both GET and POST
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("All fields are required!", "error")
            return redirect("/contact")

        messages_collection.insert_one({
            "name": name,
            "email": email,
            "message": message,
            "timestamp": datetime.now(timezone.utc)  # Store timestamp for records
        })

        flash("Your message has been sent successfully", "success")
        return redirect("/contact")

    return render_template('contact.html')
