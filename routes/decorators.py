from functools import wraps
from flask import session, redirect, url_for, flash

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            flash("You must be logged in to access this page.", "danger")
            return redirect(url_for("login"))

        if not session.get("is_admin"):
            flash("Unauthorized access.", "danger")
            return redirect(url_for("products.show_products"))  # Redirect non-admins to products page

        return f(*args, **kwargs)
    return decorated_function
