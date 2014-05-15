from app import db


class JobAccounting(db.Model):
    __tablename__ = 'job_accounting'

    id = db.Column(db.Integer, primary_key=True)
    job_accounting_first_check_amount = db.Column(db.String(64))
    job_accounting_depreciation_check_amount = db.Column(db.String(64))
    job_accounting_coupon_amount = db.Column(db.String(64))
    job_accounting_advertising_credit_amount = db.Column(db.String(64))

    def __init__(
            self,
            job_accounting_first_check_amount,
            job_accounting_depreciation_check_amount,
            job_accounting_coupon_amount,
            job_accounting_advertising_credit_amount
    ):
        self.job_accounting_first_check_amount = job_accounting_first_check_amount
        self.job_accounting_depreciation_check_amount = job_accounting_depreciation_check_amount
        self.job_accounting_coupon_amount = job_accounting_coupon_amount
        self.job_accounting_advertising_credit_amount = job_accounting_advertising_credit_amount

    def __repr__(self):
        return '<JobAccounting %r>' % self.job_accounting_first_check_amount