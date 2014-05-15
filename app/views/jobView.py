from flask import render_template, request
from app import app
from app.models.jobModel import Job
from app.controllers.jobController import get_all_jobs
from app.controllers.customerController import get_all_customer_names

@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    _jobs = get_all_jobs()
    _customer_names = get_all_customer_names()
    _customer_names.reverse()

    return render_template(
        'dash/jobs.html',
        subtitle = 'Jobs Summary',
        theme = 'superhero',
        jobs = _jobs,
        customer_names = _customer_names
    )