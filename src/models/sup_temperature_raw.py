from db import db
class TemperatureRaw(db.Model):
    __tablename__ = "sup_temperature_raw"

    pk_temperature_raw_id = db.Column(db.Integer, primary_key=True)
    action_datetime = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    wind_speed = db.Column(db.Integer, nullable=False)
    rain_intensity = db.Column(db.Integer, nullable=False)
    rain_accumulation = db.Column(db.Integer, nullable=False)