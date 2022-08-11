from flask import Flask, render_template, redirect, session, request
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secretkey = "buttcrack"


@app.route("/user")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)


@app.route("/")
@app.route("/user/new")
def create():

    return render_template("create.html")


@app.route("/user/new", methods=["post"])
def form():

    User.add_one(request.form)
    return redirect('/user')


if __name__ == "__main__":
    app.run(debug=True)
