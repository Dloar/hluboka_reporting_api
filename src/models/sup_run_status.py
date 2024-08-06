from db import db
class RunStatus(db.Model):
    __tablename__ = "sup_run_status"

    pk_run_status_id = db.Column(db.Integer, primary_key=True)
    action_datetime = db.Column(db.Date, nullable=False)
    calculation_id = db.Column(db.Integer, nullable=False)
    run_status = db.Column(db.Integer, nullable=False)
    income_input = db.Column(db.String(128), nullable=True, default=3)