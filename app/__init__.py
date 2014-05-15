# ===================================================================
# App Init - app/__init__.py
# ===================================================================
import os
from flask import Flask
from flask.ext.wtf.csrf import CsrfProtect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from jinja2 import Environment, PackageLoader

from app.config import BASE_DIR

# init app obj
app = Flask(__name__)

# init global config
app.config.from_object('app.config')

# init csrf protection
csrf = CsrfProtect()
csrf.init_app(app)

# init database/orm
db = SQLAlchemy(app)

# init login manager
lm = LoginManager()
lm.init_app(app)

# init openID support
oid = OpenID(app, os.path.join(BASE_DIR, '/../tmp'))

# init jinja2 environment
env = Environment(loader=PackageLoader('app', 'templates'))