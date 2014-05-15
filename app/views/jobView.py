from flask import render_template, request
from app import app
from app.models.jobModel import Job


@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    jobs = Job.query.all()
    return render_template(
        'dash/jobs.html',
        subtitle = 'Jobs Summary',
        theme = 'superhero',
        jobs = jobs
        # customer_names = get_all_customer_names()
    )