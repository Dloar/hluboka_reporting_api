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
    restaurace = fields.Integer(allow_none=True)
    kavarna = fields.Integer(allow_none=True)
    lanovy_park = fields.Integer(allow_none=True)
    minigolf = fields.Integer(allow_none=True)
    trampoliny = fields.Integer(allow_none=True)
    pujcovna = fields.Integer(allow_none=True)
    koktejl_bar = fields.Integer(allow_none=True)
    spunt_vstup = fields.Integer(allow_none=True)
    spunt_obcerstveni = fields.Integer(allow_none=True)
    total_employees = fields.Integer(allow_none=True)
