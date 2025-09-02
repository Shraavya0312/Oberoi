from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify

from flask_socketio import SocketIO, send

from helpers import login_required

import json

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

socketio = SocketIO(app, cors_allowed_origins="*")

db = SQL("sqlite:///data.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE name = ?", request.form.get("username"))
        if not rows:
            flash("Invalid username and/or password")
            return render_template("login.html")
        if not check_password_hash(rows[0]["password"], request.form.get("password")):
            flash("Invalid username and/or password")
            return render_template("login.html")
        return redirect("/map")
    else:
        return render_template("login.html")
    
@app.route("/signup", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":

        rows = db.execute("SELECT * FROM users WHERE name = ?", request.form.get("username"))
        if len(rows) != 0:
            flash("username already exists")
            return render_template("login.html")

        db.execute("INSERT INTO users (name, password, email) VALUES (?,?,?)",
                    request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("email"))
        rows = db.execute("SELECT * FROM users WHERE name = ?", request.form.get("username"))

        session["user_id"] = rows[0]["id"]

        return redirect("/map")
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/map")
def map():
    coors = db.execute("SELECT name, xcoor, ycoor FROM charging")
    coors_json = json.dumps(coors)
    return render_template("map.html", coors_json=coors_json)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/reg", methods=["GET", "POST"])
# @login_required
def reg():
    if request.method == "POST":
        # username = db.execute('SELECT username FROM users WHERE id = :user_id', user_id=session["user_id"])
        db.execute("INSERT INTO charging (name, xcoor, ycoor, isVerified, availibility, rating) VALUES (?,?,?,?,?,?)", "name", request.form.get("xcoor"), request.form.get("ycoor"), "F", "T", "0")
        return render_template("reg.html")
    else:
        return render_template("reg.html")