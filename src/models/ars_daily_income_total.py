from db import db


class DailyIncomeTotal(db.Model):
    __tablename__ = 'ars_daily_income_total'

    pk_daily_income_total_id = db.Column(db.Integer, primary_key=True)
    fk_day_temperature_id = db.Column(db.Integer,
                                      db.ForeignKey("ars_day_temperature.pk_day_temperature_id"),
                                      nullable=True)
    total_income = db.Column(db.Integer, primary_key=True)
    action_date = db.Column(db.Date, primary_key=True)