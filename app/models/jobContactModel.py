from app import db


class JobContact(db.Model):
    __tablename__ = 'job_contact'

    id = db.Column(db.Integer, primary_key=True)
    job_contact_alternate_name = db.Column(db.String(64))
    job_contact_alternate_type = db.Column(db.String(32))
    job_contact_alternate_primary_phone = db.Column(db.String(10))
    job_contact_alternate_other_phone = db.Column(db.String(10))
    job_contact_alternate_email = db.Column(db.String(255))

    def __init__(
            self,
            job_contact_alternate_name,
            job_contact_alternate_type,
            job_contact_alternate_primary_phone,
            job_contact_alternate_other_phone,
            job_contact_alternate_email
    ):
        self.job_contact_alternate_name = job_contact_alternate_name
        self.job_contact_alternate_type = job_contact_alternate_type
        self.job_contact_alternate_primary_phone = job_contact_alternate_primary_phone
        self.job_contact_alternate_other_phone = job_contact_alternate_other_phone
        self.job_contact_alternate_email = job_contact_alternate_email