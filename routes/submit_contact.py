from flask import Blueprint, render_template

submit_contact_bp = Blueprint('submit_contact', __name__)

@submit_contact_bp.route('/submit_contact')
def submit_contact():
    return render_template('submit_contact.html')