from flask import flash, render_template, redirect
from app import app
from app.forms.loginForm import LoginForm


# login route
@app.route('/login', methods=['GET', 'POST'])
def show_login():

    form = LoginForm()

    return render_template(
        'forms/loginForm.html',
        subtitle='Sign In',
        theme='superhero',
        form=form
    )
