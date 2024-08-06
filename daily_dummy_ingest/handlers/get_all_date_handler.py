from src.queries.handlers.get_weather_day_detail_data_handler import GetWeatherDayDetailDataHandler


class GetAllDataHandler:
    """
    Load all necessary data for campaign optimization
    """

    @staticmethod
    def get_daily_temperatures():
        daily_temperature_df = GetWeatherDayDetailDataHandler().load_weather_day_detail_data()

        return daily_temperature_df

