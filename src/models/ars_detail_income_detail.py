from db import db


class DailyIncomeDetail(db.Model):
    __tablename__ = 'ars_daily_income_detail'

    pk_daily_income_detail_id = db.Column(db.Integer, primary_key=True)
    fk_attraction_dictionary_id = db.Column(db.Integer,
                                            db.ForeignKey("ars_attraction_dictionary.pk_attraction_dictionary_id"),
                                            nullable=True)
    fk_day_temperature_id = db.Column(db.Integer,
                                      db.ForeignKey("ars_day_temperature.pk_day_temperature_id"),
                                      nullable=True)
    attraction_income = db.Column(db.Integer, nullable=True)
    action_date = db.Column(db.Date, nullable=True)