from db import db
class UserModel(db.Model):
    __tablename__ = "ssy_user"

    pk_user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128))
    user_function = db.Column(db.String(128))