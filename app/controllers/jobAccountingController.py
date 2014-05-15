from app.models.jobAccountingModel import JobAccounting


def get_acct(pk):
    acct = JobAccounting.query.filter_by(id=pk).all()
    return acct



