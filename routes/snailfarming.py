from flask import Blueprint, render_template, request, flash, redirect
from db.dbconnection import db
import pytz
from datetime import datetime, timezone 


wat = pytz.timezone("Africa/Lagos")  # Lagos, Nigeria (WAT)

snailfarming_collection = db["snailfarming"]

snailfarming_bp = Blueprint('snailfarming', __name__)

@snailfarming_bp.route('/snailfarming', methods=["GET", "POST"])
def snailfarming():
    if request.method == 'POST':
        trainingtype = request.form.get("trainingtype")
        name = request.form.get("name")
        email = request.form.get("email")
        phonenumber = request.form.get("phonenumber")
        message = request.form.get("message")

        if not name or not email or not phonenumber:
            flash("Please Enter Required Information")
            return redirect("/snailfarming")
        snailfarming_collection.insert_one({
            "trainingtype": trainingtype,
            "name": name,
            "email": email,
            "phonenumber": phonenumber,
            "message": message,
            "timestamp": datetime.now(wat)
        })
        flash("Your message has been sent successfully", "success")
        return redirect("/services")
    return render_template('snailfarming.html')