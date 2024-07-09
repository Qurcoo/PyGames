from ext import app, db
from models import Product, Uplposts

with app.app_context():
    db.create_all()
    admin_user = User("admin", "password321","admin")
    db.session.add(admin_user)
    db.session.commit()
