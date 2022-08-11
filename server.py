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
def create():  # creating a new user
    return render_template("create.html")


@app.route("/user/new", methods=["post"])  # The form for creating a new user
def form():
    User.add_one(request.form)
    return redirect('/user')


@app.route("/user/<int:num>")  # will return only one users info
def user_info(num):
    data = {"id": num}
    get_user = User.get_one(data)
    return render_template("read_one.html", get_user=get_user)


@app.route("/user/edit/<int:id>")
def edit(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("edit.html", user=User.get_one(data))


@app.route("/destroy/<int:id>")
def delete(id):
    User.delete({"id": id})
    return redirect("/user")


@app.route("/user/update/<int:id>", methods=["POST"])
def update(id):
    print("**************************************************************************")
    User.update(request.form)
    return redirect(f'/user/{id}')


if __name__ == "__main__":
    app.run(debug=True)
