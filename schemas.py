from marshmallow import Schema, fields

class WeatherSchema(Schema):
    action_datetime = fields.DateTime(required=True)
    temperature = fields.Integer(allow_none=True)
    humidity = fields.Integer(allow_none=True)
    wind_speed = fields.Integer(allow_none=True)
    rain_intensity = fields.Integer(allow_none=True)
    rain_accumulation = fields.Integer(allow_none=True)


class IncomeSchema(Schema):
    action_date = fields.Date(required=True)
    attraction_name = fields.Str(required=True)
    attraction_income = fields.Integer(required=True)