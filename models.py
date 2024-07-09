from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    image = db.Column(db.String())

class Uplposts(db.Model):
    __tablename__ = "uplposts"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    abtGame = db.Column(db.String())
    email = db.Column(db.String())

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    def __init__(self,username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password) 

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user
