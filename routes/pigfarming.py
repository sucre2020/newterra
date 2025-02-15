from flask import Blueprint, render_template, request, flash, redirect
from db.dbconnection import db
from datetime import datetime, timezone

pigfarming_collection = db["pigfarming"]

pigfarming_bp = Blueprint('pigfarming', __name__)

@pigfarming_bp.route('/pigfarming', methods=["GET", "POST"])
def pigfarming():
    if request.method == "POST":
        trainingtype = request.form.get("trainingtype")
        name = request.form.get("name")
        email = request.form.get("email")
        phonenumber = request.form.get("phonenumber")
        message = request.form.get("message")
        if not name or not email or not phonenumber:
            flash("Please Enter Required Information")
            return redirect("/pigfarming")
        pigfarming_collection.insert_one({
            "trainingtype": trainingtype,
            "name": name,
            "email": email,
            "phonenumber": phonenumber,
            "message": message,
            "timestamp": datetime.now(timezone.utc)
        })
        flash("Your message has been sent successfully", "success")
        return redirect("/services")
    return render_template("pigfarming.html")




