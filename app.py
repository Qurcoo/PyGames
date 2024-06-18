from ext import app


if __name__ == "__main__":
    from routes import index, index2, game, dwnld, index4, gamesF, post, uplPosts1, delete, edit_user, tbc
    app.run(debug = True)