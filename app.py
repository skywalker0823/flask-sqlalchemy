from flask import Flask, render_template as rt, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database.control import BookController


# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__, template_folder="templates")
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


# new_book = BookController()
# new_book.Create("The Hobbit", "J.R.R. Tolkien", "Fantasy")


@app.route("/")
def index():
    new_book = BookController()
    books = new_book.Read_all()
    print(books)
    print(type(books))
    print(books[0].title)
    return rt("index.html", books=books)

@app.route("/create", methods=["GET"])
def create():
    new_book = BookController()
    result = new_book.Create("The Hobbit", "J.R.R. Tolkien", "Fantasy")
    print(result)
    if result:
        return "OK"
    else:
        return "Error"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


