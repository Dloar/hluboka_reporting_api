# Adwiro 2022
# Get billboard source data

class GetWeatherDayRawDataQuery:

    @staticmethod
    def query_weather_day_raw_data():
        day_raw_data = f''' 
                        select * 
                        from sup_temperature_raw;'''
        return day_raw_data
