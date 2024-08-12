from src.queries.handlers.get_attraction_daily_data_handler import GetAttractionDailyDataHandler
from src.queries.handlers.get_attraction_data_handler import GetAttractionDataHandler
from src.queries.handlers.get_weather_day_detail_data_handler import GetWeatherDayDetailDataHandler
from src.queries.handlers.get_weather_day_raw_data_handler import GetWeatherDayRawDataHandler


class GetIncomeDataHandler:
    def __init__(self, income_data):
        self.daily_income_df = GetAttractionDailyDataHandler().load_attraction_daily_data()
        self.calendar_detail_df = GetWeatherDayDetailDataHandler().load_weather_day_detail_data()
        self.raw_temperature_df = GetWeatherDayRawDataHandler().load_weather_day_raw_data()
        self.attraction_data_df = GetAttractionDataHandler().load_attraction_data()
        self.processing_date = income_data['action_date']



