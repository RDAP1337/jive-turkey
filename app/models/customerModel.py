from app import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(64), unique=True)
    customer_name = db.Column(db.String(64))
    customer_primary_phone = db.Column(db.String(10))
    customer_other_phone = db.Column(db.String(10))
    customer_email = db.Column(db.String(256))
    customer_street_1 = db.Column(db.String(64))
    customer_street_2 = db.Column(db.String(64))
    customer_city = db.Column(db.String(32))
    customer_state = db.Column(db.String(2))
    customer_zip = db.Column(db.String(5))
    customer_created = db.Column(db.DateTime)
    customer_modified = db.Column(db.DateTime)

    def __init__(
            self,
            customer_id,
            customer_name,
            customer_primary_phone,
            customer_other_phone,
            customer_email,
            customer_street_1,
            customer_street_2,
            customer_city,
            customer_state,
            customer_zip,
            customer_created,
            customer_modified
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_primary_phone = customer_primary_phone
        self.customer_other_phone = customer_other_phone
        self.customer_email = customer_email
        self.customer_street_1 = customer_street_1
        self.customer_street_2 = customer_street_2
        self.customer_city = customer_city
        self.customer_state = customer_state
        self.customer_zip = customer_zip
        self.customer_created = customer_created
        self.customer_modified = customer_modified