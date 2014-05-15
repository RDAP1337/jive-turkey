from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class ModifyUser(Form):
    username = TextField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    admin = BooleanField('admin')