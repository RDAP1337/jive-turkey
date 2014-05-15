from app import db


class SalesRep(db.Model):
    __tablename__ = 'sales_rep'

    id = db.Column(db.Integer, primary_key=True)
    sales_rep_id = db.Column(db.String(64), unique=True)
    sales_rep_first_name = db.Column(db.String(32))
    sales_rep_last_name = db.Column(db.String(32))
    sales_rep_username = db.Column(db.String(64))
    sales_rep_phone = db.Column(db.String(10))
    sales_rep_email = db.Column(db.String(256))
    sales_rep_created = db.Column(db.DateTime)
    sales_rep_modified = db.Column(db.DateTime)

    def __init__(
            self,
            sales_rep_id,
            sales_rep_first_name,
            sales_rep_last_name,
            sales_rep_username,
            sales_rep_phone,
            sales_rep_email,
            sales_rep_created,
            sales_rep_modified
    ):
        self.sales_rep_id = sales_rep_id
        self.sales_rep_first_name = sales_rep_first_name
        self.sales_rep_last_name = sales_rep_last_name
        self.sales_rep_username = sales_rep_username
        self.sales_rep_phone = sales_rep_phone
        self.sales_rep_email = sales_rep_email
        self.sales_rep_created = sales_rep_created
        self.sales_rep_modified = sales_rep_modified