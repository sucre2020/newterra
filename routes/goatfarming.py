from flask import Blueprint, render_template, request, flash, redirect
from db.dbconnection import db
from datetime import datetime, timezone


goatfarming_collection = db["goatfarming"]

goatfarming_bp = Blueprint('goatfarming', __name__)

@goatfarming_bp.route("/goatfarming", methods=["GET", "POST"])
def goatfarming():
    if request.method == 'POST':
        trainingtype = request.form.get("trainingtype")
        name = request.form.get("name")
        email = request.form.get("email")
        phonenumber = request.form.get("phonenumber")
        message = request.form.get("message")

        if not name or not email or not phonenumber:
            flash("Please Enter Required Information")
            return redirect("/goatfarming")
        goatfarming_collection.insert_one({
            "trainingtype": trainingtype,
            "name": name,
            "email": email,
            "phonenumber": phonenumber,
            "message": message,
            "timestamp": datetime.now(timezone.utc)
        })
        flash("Your message has been sent successfully", "success")
        return redirect("/services")

    return render_template("goatfarming.html")