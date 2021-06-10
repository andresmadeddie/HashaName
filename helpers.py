import os
import requests
import random

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("userid") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# Return a dictionary with 5 random keys to use in encoding function
def randomkey():
    n = random.randrange(1, 62)  # Range to decrease current character ASCII number to another valid ASCII character bigger than 32
    number = chr(random.randrange(48, 57))  # Range of numbers in ASCII
    upper = chr(random.randrange(65, 90))  # Range of uppercase in ASCII
    lower = chr(random.randrange(97, 122))  # Range of lowercase in ASCII
    symbol = random.randint(0, 27)  # Choose and integer from a range of special characters defined in the encoding function

    # Create dictionary with previous values
    keys = {"n": n, "number": number, "upper": upper, "lower": lower, "symbol": symbol}

    return keys


# Returns a password STRING from input data keyword(only alphabet characters) and keys(dictionary)
def encode(keyword, keys):

    # initiate password as a list
    password = []

    # Add to symbols all symbols from ascii table for reference validation
    symbols = []
    for i in range(33, 47):
        symbols.append(chr(i))
    for i in range(58, 64):
        symbols.append(chr(i))
    for i in range(91, 96):
        symbols.append(chr(i))
    for i in range(123, 126):
        symbols.append(chr(i))

    # Update key variables from received algorithm key
    n = keys["n"]
    number = keys["number"]
    upper = keys["upper"]
    lower = keys["lower"]
    symbol = keys["symbol"]

    # Transform all characters to lowercase
    keyword = keyword.lower()

    # Enconde keyword decreasing its ASCII value by n
    for i in keyword:
        password.append(chr(ord(i)-n))

    # Transform password from LIST into a STRING
    password = "".join(password)

    # Add number to string if none
    if not any(char.isdigit() for char in password):
        password = password + number
    # Add uppercase to string if none
    if not any(char.isupper() for char in password):
        password = password + upper
    # Add lowercase to string if none
    if not any(char.islower() for char in password):
        password = password + lower
    # Add symbol to string if none
    if not any(char in symbols for char in password):
        password = password + symbols[symbol]
    # Ensure that password be at least 8 characters long
    if len(password) < 8:
        n = 8 - len(password)
        for i in range(n):
            password = password + symbols[i]

    return password
#  https://www.geeksforgeeks.org/password-validation-in-python/
