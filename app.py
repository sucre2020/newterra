from flask import Flask, render_template
from dotenv import load_dotenv
from flask import session
import os
load_dotenv()
from routes.home import home_bp
from routes.about import about_bp
from routes.cart import cart_bp
from routes.contact import contact_bp
from routes.layout import layout_bp
from routes.login import login_bp
from routes.products import products_bp
from routes.services import services_bp
from routes.stories_projects import stories_projects_bp
from routes.submit_contact import submit_contact_bp
from routes.auth_routes import auth_bp
from routes.goatfarming import goatfarming_bp
from routes.pigfarming import pigfarming_bp
from routes.snailfarming import snailfarming_bp
from routes.turkeyfarming import turkeyfarming_bp
from routes.horsefarming import horsefarming_bp
from routes.admin_routes import admin_bp
from routes.search import search_bp



app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(layout_bp)
app.register_blueprint(login_bp)
app.register_blueprint(products_bp)
app.register_blueprint(services_bp)
app.register_blueprint(stories_projects_bp)
app.register_blueprint(submit_contact_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(goatfarming_bp)
app.register_blueprint(pigfarming_bp)
app.register_blueprint(snailfarming_bp)
app.register_blueprint(turkeyfarming_bp)
app.register_blueprint(horsefarming_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(search_bp)

@app.context_processor
def inject_cart_item_count():
    cart = session.get('cart', [])
    cart_item_count = sum(item['quantity'] for item in cart)
    return {'cart_item_count': cart_item_count}



if __name__ == '__main__':
    app.run(debug=True)
