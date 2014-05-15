from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired
from app.forms import BaseForm


# LoginForm Class
#
# param = Form Object
class LoginForm(BaseForm):

    username = TextField(
        'username',
        validators=[DataRequired()]
    )

    password = PasswordField(
        'password',
        validators=[DataRequired()]
    )