from flask import Blueprint, render_template, request, flash, redirect
from db.dbconnection import db
from datetime import datetime, timezone

horsefarming_collection = db["horsefarming"]

horsefarming_bp = Blueprint('horsefarming', __name__)

@horsefarming_bp.route('/horsefarming', methods=["GET", "POST"])
def horsefarming():
    if request.method == "POST":
        trainingtype = request.form.get("trainingtype")
        name = request.form.get("name")
        email = request.form.get("email")
        phonenumber = request.form.get("phonenumber")
        message = request.form.get("message")
        if not name or not email or not phonenumber:
            flash("Please Enter Required Information")
            return redirect("/horsefarming")
        horsefarming_collection.insert_one({
            "trainingtype": trainingtype,
            "name": name,
            "email": email,
            "phonenumber": phonenumber,
            "message": message,
            "timestamp": datetime.now(timezone.utc)
        })
        flash("Your message has been sent successfully", "success")
        return redirect("/services")
    return render_template('horsefarming.html')