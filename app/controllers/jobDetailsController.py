from app.models.jobDetailsModel import JobDetails


def get_all_job_details():
    job_details = JobDetails.query.all()
    return job_details