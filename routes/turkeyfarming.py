from flask import Blueprint, render_template, request, flash, redirect
from db.dbconnection import db
from datetime import datetime, timezone

turkeyfarming_collection = db["turkeyfarming"]

turkeyfarming_bp = Blueprint('turkeyfarming', __name__)

@turkeyfarming_bp.route('/turkeyfarming', methods=["GET", "POST"])
def turkeyfarming():
    if request.method == 'POST':
        trainingtype = request.form.get("trainingtype")
        name = request.form.get("name")
        email = request.form.get("email")
        phonenumber = request.form.get("phonenumber")
        message = request.form.get("message")

        if not name or not email or not phonenumber:
            flash("Please Enter Required Information")
            return redirect("/turkeyfarming")
        turkeyfarming_collection.insert_one({
            "trainingtype": trainingtype,
            "name": name,
            "email": email,
            "phonenumber": phonenumber,
            "message": message,
            "timestamp": datetime.now(timezone.utc)
        })
        flash("Your message has been sent successfully", "success")
        return redirect("/services")
    return render_template('turkeyfarming.html')