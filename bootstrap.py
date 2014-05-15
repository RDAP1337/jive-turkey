#!/usr/bin/env python2

from app.models.jobModel import db as jobs_db
from app.models.salesRepModel import db as sales_rep_db
from app.models.customerModel import db as customer_db
from app.models.jobDetailsModel import db as job_details_db
from app.models.jobMaterialsModel import db as job_materials_db
from app.models.jobChecklistModel import db as job_checklist_db
from app.models.jobAccountingModel import db as job_accounting_db
from app.models.jobContactModel import db as job_contact_db
from app.models.userModel import db as users_db
from app.models.userModel import User
from app.controllers.securityController import new_password

jobs_db.create_all()
job_details_db.create_all()
job_materials_db.create_all()
job_checklist_db.create_all()
job_accounting_db.create_all()
job_contact_db.create_all()
sales_rep_db.create_all()
customer_db.create_all()
users_db.create_all()

admin = User('admin', new_password('password'), 1, 1)
users_db.session.add(admin)
users_db.session.commit()