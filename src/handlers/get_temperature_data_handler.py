from src.queries.handlers.get_weather_day_detail_data_handler import GetWeatherDayDetailDataHandler
from src.queries.handlers.get_weather_day_raw_data_handler import GetWeatherDayRawDataHandler


class GetTemperatureDataHandler:
    def __init__(self):
        self.daily_weather = GetWeatherDayDetailDataHandler().load_weather_day_detail_data()
        self.raw_weather = GetWeatherDayRawDataHandler().load_weather_day_raw_data()

    def process_temperature_data(self, temperature_data):
        pass

