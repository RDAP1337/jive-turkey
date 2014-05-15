from flask import Blueprint
from wtforms.ext.csrf.session import SessionSecureForm
from app.config import SECRET_KEY

forms = Blueprint('forms', __name__)


class BaseForm(SessionSecureForm):
    secret_key = SECRET_KEY
    time_limit = None