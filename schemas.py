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
    restaurace = fields.Integer(required=True)
    kavarna = fields.Integer(required=True)
    lanovy_park = fields.Integer(required=True)
    minigolf = fields.Integer(required=True)
    trampoliny = fields.Integer(required=True)
    pujcovna = fields.Integer(required=True)
    koktejl_bar = fields.Integer(required=True)
    spunt_vstup = fields.Integer(required=True)
    spunt_obcerstveni = fields.Integer(required=True)
