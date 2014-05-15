from flask import Blueprint

views = Blueprint('views', __name__)

import indexView
import jobView
import customerView
import loginView
import securityView
import salesRepView
import userView