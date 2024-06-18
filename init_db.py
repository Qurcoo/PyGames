from ext import app, db
from models import Product, Uplposts

with app.app_context():
    db.create_all()
