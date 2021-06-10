import os

from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, randomkey , encode


# Configure application
app = Flask(__name__)

#######################################################################################################################
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
#######################################################################################################################

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data.db")


@app.route("/", methods=["GET", "POST"])
def index():

    # User reached route via POST
    if request.method == "POST":

        # Redirect to login
        if request.form.get("login"):
            return redirect("/login")

        # Redirect to guest
        if request.form.get("guest"):
            flash("Guest Mode can`t store keys. Data will be lost after session expired.")
            return redirect("/guest")

        # Redirect to register
        if request.form.get("register"):
            return redirect("/register")

    # User reached route via GET
    else:
        # Ensure user has log in
        if 'userid' in session:
            return redirect("/user")
        else:
            return render_template("index.html")


@app.route("/user", methods=["GET", "POST"])
@login_required
def user():

    # User reached route via POST
    if request.method == "POST":

        # CHANGE password's algorithm key
        if request.form.get("change"):
            session["keys"] = randomkey()
            flash("Password's algorithm key Changed.")
            return redirect("/user")

        # GET password
        if request.form.get("keyword"):
            keyword = request.form.get("keyword")
            keys = session["keys"]
            password = encode(keyword, keys)
            session['password'] = password  # Store in session for update need
            return redirect("/user")

        # SAVE password's algorithm key
        if request.form.get("save"):
            keyname = request.form.get("save")
            dt = datetime.now()
            n = session["keys"]["n"]
            number = session["keys"]["number"]
            upper = session["keys"]["upper"]
            lower = session["keys"]["lower"]
            symbol = session["keys"]["symbol"]

            db.execute("INSERT INTO data (userid, datetime, n, number, upper, lower, symbol, keyname) VALUES (:userid, :datetime, :n, :number, :upper, :lower, :symbol, :keyname)", userid=session["userid"], datetime=dt, n=n, number=number, upper=upper, lower=lower, symbol=symbol, keyname=keyname)
            return redirect("/user")

        # SELECT stored password's algorithm key
        if request.form.get("select"):
            session["keys"] = db.execute("SELECT n, number, upper, lower, symbol FROM data WHERE userid=:userid AND id=:id", userid=session["userid"], id=request.form.get("select"))[0]  # The "[0]"" is fo take the dictionary out of the list for compatibility
            return redirect("/user")

        # DELETE stored password's algorithm key
        if request.form.get("delete"):
            db.execute("DELETE FROM data WHERE userid=:userid AND id=:id", userid=session["userid"], id=request.form.get("delete"))
            return redirect("/user")

        # DELETE ALL store password's algorithm key
        if request.form.get("deleteall"):
            db.execute("DELETE FROM data WHERE userid=:userid", userid=session["userid"])
            return redirect("/user")

    # User reached route via GET
    else:

        # Ensure there are no keys are stored in session
        if not 'keys' in session:

            # Query database
            rows = db.execute("SELECT * FROM data WHERE userid=:userid ORDER BY datetime", userid=session["userid"])

            # Ensure no keys are stored in database
            if len(rows) == 0:
                session["keys"] = randomkey()
            else:
                session["keys"] = rows[0]

        # Query database for stored keys id and datetime
        idkeyname = db.execute("SELECT id, datetime, keyname FROM data WHERE userid = :userid", userid=session["userid"])

        # Ensure no password is stored in session
        password = None
        if 'password' in session:
            password = session['password']

        # Redirect to user with all collected values
        return render_template("user.html", idkeyname=idkeyname, password=password)


@app.route("/guest", methods=["GET", "POST"])
def guest():

    # User reached route via POST
    if request.method == "POST":

        # Ensure there is a key in session
        if "keys" not in session:
            session["keys"] = randomkey()

        # CHANGE password's algorithm key
        if request.form.get("change"):
            session["keys"] = randomkey()
            flash("Guest Mode: Password's algorithm key changed, but will be lost after the session ends.")
            return redirect("/guest")

        # GET password
        if request.form.get("keyword"):
            keyword = request.form.get("keyword")
            keys = session["keys"]
            password = encode(keyword, keys)
            flash("Guest Mode: The current password's algorithm key will be lost after the session ends.")
            return render_template("guest.html", password=password)

    # User reached route via GET
    else:
        # Redirect to guest template
        return render_template("guest.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any userid
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)#########################################################modify

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)#########################################################modify

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hashkey"], request.form.get("password")):
            return apology("invalid username and/or password", 403)#########################################################modify

        # Remember which user has logged in
        session["userid"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET
    else:
        # Redirect user to login template
        return render_template("login.html")


@app.route("/logout")
def logout():

    # Forget any userid
    session.clear()

    # Redirect user to home page
    return redirect("/")

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():

    # User reached route via POST
    if request.method == "POST":
        # Delete all data of current user and clear current session
        db.execute("DELETE FROM data WHERE userid=:userid", userid=session["userid"])
        db.execute("DELETE FROM users WHERE id=:userid", userid=session["userid"])
        session.clear()
        flash("Account Closed")
        return render_template("login.html")
    else:
        return render_template("account.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    # Forget any userid
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)#########################################################modify

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)#########################################################modify

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 403)#########################################################modify

        # Ensure that confirmation match password
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("confirmation do not match password", 403)#########################################################modify

        # Store values in variables
        username = request.form.get("username")  # Store name
        hash1 = generate_password_hash(request.form.get("password"))  # Store the hash of the password

        # Upload new information in database with secure method againts SQL injection
        db.execute("INSERT INTO users (username, hashkey) VALUES (:username, :hashkey)", username=username, hashkey=hash1)

        # Redirect user to home page
        return redirect("/login")

    # User reached route via GET
    else:
        # Redirect user to register template
        return render_template("/register.html")

@app.route("/help", methods=["GET", "POST"])
def help():
    return render_template("/help.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)