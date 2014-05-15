from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(140))
    admin = db.Column(db.Boolean())
    rep = db.Column(db.Boolean())

    def __init__(
            self,
            username,
            password,
            admin,
            rep
    ):
        self.username = username
        self.password = password
        self.admin = admin
        self.rep = rep

    def is_admin(self):
        return self.admin

    def is_rep(self):
        return self.rep