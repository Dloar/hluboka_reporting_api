from db import db


class DayTemperature(db.Model):
    __tablename__ = 'ars_day_temperatury'

    pk_day_temperature_id = db.Column(db.Integer, primary_key=True)
    action_date = db.Column(db.Date, primary_key=True)
    temperature = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Integer, primary_key=True)
    wind_speed = db.Column(db.Integer, primary_key=True)
    rain_intensity = db.Column(db.Integer, primary_key=True)
    rain_accumulation = db.Column(db.Integer, primary_key=True)
    time_of_sun = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.Integer, primary_key=True)