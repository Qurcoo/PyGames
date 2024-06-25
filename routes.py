from flask import render_template, redirect
from forms import PostForm, EditUserForm, RegisterForm, LoginForm
from flask_login import login_user
from models import Product, Uplposts, User
from ext import app, db



products = [
    {"Name": "COD", "Price": "50", "image": "/static/COD.jpg", "id": 0},
    {"Name": "The Forest", "Price": "55", "image": "/static/Forest.png", "id": 1},
    {"Name": "Dying Light", "Price": "74", "image": "/static/dying light.jpg", "id": 2},
    {"Name": "The Last Of Us", "Price": "30", "image": "/static/last of us.jpg", "id": 3},
    {"Name": "PUBG", "Price": "35", "image": "/static/PUBG.webp", "id": 4},
    ]

posts = [

]


@app.route("/")
def index():
    return render_template("main.html")

@app.route("/game/<int:gameid>")
def game(gameid):
    return render_template("game.html", game=products[gameid])

@app.route("/Login", methods=["GET", "POST"])
def index2():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            print(user)
            return redirect("/")
    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET", "POST"])
def index4():
    form = RegisterForm()
    
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if not user:
            new_user = User(username=form.username.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/Login")
    return render_template("signup.html", form=form)


@app.route("/download")
def dwnld():
    return render_template("download.html")

@app.route("/games")
def gamesF():
    return render_template("games.html", games=products)


@app.route("/post", methods=["POST", "GET"])
def post():
    
    form = PostForm()
    if form.validate_on_submit():
        users_post = Uplposts(email=form.email.data, File_inp=form.File_inp.data.filename, abtGame=form.abtGame.data)
        db.session.add(users_post)
        db.session.commit()
        
        image = form.File_inp.data
        image.save(f"{app.root_path}\static\{image.filename}")

        print(users_post)
    return render_template("post.html", form=form)

@app.route("/posts", methods=["POST","GET"])
def uplPosts1():
    posts = Uplposts.query.all()
    return render_template("posts.html", posts=posts)

@app.route("/delete/<int:user_id>")
def delete(user_id):
    exactpost = Uplposts.query.get(user_id)
    db.session.delete(exactpost)
    db.session.commit()
    return redirect("/posts")

@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    thispost = Uplposts.query.get(user_id)
    form = EditUserForm(username=thispost.username, email=thispost.email, abtGame=thispost.abtGame)
    if form.validate_on_submit():
        thispost.username = form.username.data
        thispost.email = form.email.data
        thispost.abtGame = form.abtGame.data
        thispost.File_inp = form.File_inp.data.filename
        image = form.File_inp.data
        image.save(f"{app.root_path}\static\{image.filename}")
        db.session.commit()
        return redirect("/posts")



    return render_template("edit_user.html", form=form)

@app.route("/tbc")
def tbc():
    return redirect("https://www.tbceducation.ge")

if User.username == "giorgi":
    Role = "Admin"
else:
    Role = "user"
