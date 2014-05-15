from flask import Blueprint

models = Blueprint('models', __name__)

import userModel
import jobModel
import customerModel
import jobAccountingModel
import jobChecklistModel
import jobContactModel
import jobDetailsModel
import jobMaterialsModel