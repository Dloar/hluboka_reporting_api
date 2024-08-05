# Adwiro 2022
# Get billboard source data

class GetWeatherDayDetailDataQuery:

    @staticmethod
    def query_weather_day_detail_data():
        day_detail_data = f''' 
                        select * 
                        from ars_day_temperature;'''
        return day_detail_data
