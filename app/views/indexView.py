from flask import render_template

from app import app
#from app.controllers.securityController import login_required
from app.controllers.jobController import get_job, get_job_id, get_job_customer_id, get_job_sales_rep_id


@app.route('/')
@app.route('/index')
#@login_required
def index():

    return  render_template(
        'dash/job_summary.html',
        subtitle = 'Home',
        theme = 'superhero',
        all_quantity = 1,
        all_premium = 1,
        open_quantity = 1,
        open_premium = 1,
        closed_quantity = 1,
        closed_premium = 1
    )