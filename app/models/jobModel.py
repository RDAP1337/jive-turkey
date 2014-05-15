from app import db


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.String(64), unique=True)
    job_created = db.Column(db.DateTime)
    job_modified = db.Column(db.DateTime)
    job_sales_rep_id = db.Column(db.String(64), unique=True)
    job_customer_id = db.Column(db.String(64), unique=True)

    def __init__(
            self,
            job_id,
            job_created,
            job_modified,
            job_sales_rep_id,
            job_customer_id
    ):
        self.job_id = job_id
        self.job_created = job_created
        self.job_modified = job_modified
        self.job_sales_rep_id = job_sales_rep_id
        self.job_customer_id = job_customer_id