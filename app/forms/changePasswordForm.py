from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired


class ChangePassword(Form):
    username = TextField('username', validators=[DataRequired()])
    oldpass = PasswordField('oldpass', validators=[DataRequired()])
    newpass1 = PasswordField('newpass1', validators=[DataRequired()])
    newpass2 = PasswordField('newpass2', validators=[DataRequired()])