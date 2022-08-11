# import the class from friend.py
from flask_app import app
from flask_app.controllers import users


app.secretkey = "buttcrack"


if __name__ == "__main__":
    app.run(debug=True)
