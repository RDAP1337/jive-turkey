from app.models.jobModel import Job


def get_all_jobs():
    jobs = Job.query.all()
    return jobs


def get_job(pk):
    job = Job.query.get(pk)
    return job


def get_job_id(job):
    return job.job_id


def get_job_customer_id(job):
    return job.job_customer_id


def get_job_sales_rep_id(job):
    return job.job_sales_rep_id


def get_job_created(job):
    return job.job_created


def get_job_modified(job):
    return job.job_modified