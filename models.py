from ext import db, login_manager
from flask_login import UserMixin

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    image = db.Column(db.String())

class Uplposts(db.Model):
    __tablename__ = "uplposts"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    File_inp = db.Column(db.String())
    abtGame = db.Column(db.String())
    email = db.Column(db.String())

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user