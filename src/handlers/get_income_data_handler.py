from src.queries.handlers.get_attraction_daily_data_handler import GetAttractionDailyDataHandler
from src.queries.handlers.get_weather_day_detail_data_handler import GetWeatherDayDetailDataHandler


class GetIncomeDataHandler:
    def __init__(self, income_data):
        self.daily_income_df = GetAttractionDailyDataHandler().load_attraction_daily_data()
        self.calendar_detail_df = GetWeatherDayDetailDataHandler().load_weather_day_detail_data()
        self.processing_date = income_data['action_date']



