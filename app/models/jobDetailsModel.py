from app import db


class JobDetails(db.Model):
    __tablename__ = 'job_details'

    id = db.Column(db.Integer, primary_key=True)
    job_details_type = db.Column(db.String(32))
    job_details_status = db.Column(db.String(32))
    job_details_location = db.Column(db.String(64))
    job_details_description_of_loss = db.Column(db.String(256))
    job_details_date_of_loss = db.Column(db.DateTime)
    job_details_start_date = db.Column(db.DateTime)
    job_details_estimated_end_date = db.Column(db.DateTime)
    job_details_needs = db.Column(db.String(256))
    job_details_peril = db.Column(db.String(64))
    job_details_source = db.Column(db.String(64))
    job_details_special_comments = db.Column(db.String(256))

    def __init__(
            self,
            job_details_type,
            job_details_status,
            job_details_location,
            job_details_description_of_loss,
            job_details_date_of_loss,
            job_details_start_date,
            job_details_estimated_end_date,
            job_details_needs,
            job_details_peril,
            job_details_source,
            job_details_special_comments
    ):
        self.job_details_type = job_details_type
        self.job_details_status = job_details_status
        self.job_details_location = job_details_location
        self.job_details_description_of_loss = job_details_description_of_loss
        self.job_details_date_of_loss = job_details_date_of_loss
        self.job_details_start_date = job_details_start_date
        self.job_details_estimated_end_date = job_details_estimated_end_date
        self.job_details_needs = job_details_needs
        self.job_details_peril = job_details_peril
        self.job_details_source = job_details_source
        self.job_details_special_comments = job_details_special_comments

    def __repr__(self):
        return '<JobDetails %r>' % self.job_details_location