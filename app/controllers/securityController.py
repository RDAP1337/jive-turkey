from flask import redirect, session, url_for, request
from functools import wraps
from app.models.userModel import User
from app.views.loginView import show_login
import random
import hashlib


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'logged_in' not in session:
            return redirect(url_for('show_login'))

        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = User.query.filter_by(username=session['username']).first()

        if user.admin is False:
            return redirect(url_for('admin'))

        return f(*args, **kwargs)

    return decorated_function


def check_password(plaintext, hashtext):
    salt = hashtext[0:8]
    crypted = hashtext[9:]

    if hashlib.sha512(plaintext + salt).hexdigest() == crypted:
        return True

    return False


def new_password(password):
    chars = []

    for i in range(8):
        chars.append(random.choice('123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    return "".join(chars) + '$' + hashlib.sha512(password + "".join(chars)).hexdigest()