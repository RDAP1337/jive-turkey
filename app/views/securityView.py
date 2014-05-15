from flask import g, redirect, session, url_for, request, render_template
from flask.ext.login import current_user
from app import app
from app.forms.loginForm import LoginForm


@app.route('/security', methods=['GET', 'POST'])
def login():
    return 'okay'