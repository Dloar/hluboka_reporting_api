from datetime import datetime

import pandas as pd
import requests as requests


class GetApiWeatherReportHandler:
    def __init__(self, processing_date):
        self.api_key = 'hPlHN6NyhI2hUgF9GSeG2BWc0ORHWIyw'
        self.processing_date = processing_date
        self.place = '49.0425636, 14.4433767'
        self.base_url = 'https://api.tomorrow.io/v4/timelines'
        self.forecast_data_df = self.load_forecast()
        # self.define_date = self.load_date_of_interest()

    def load_forecast(self):
        # Define the parameters for the API call
        params = {
            'location': self.place,  # Latitude and longitude of the location
            'fields': ['temperature', 'humidity', 'windSpeed', 'rainIntensity',
                       'rainAccumulation', 'sunriseTime', 'sunsetTime'],
            'units': 'metric',  # Use 'imperial' for Fahrenheit
            'timesteps': '1d',
            'startTime': 'nowMinus1d',
            'endTime': 'nowPlus5d',
            'apikey': self.api_key
        }

        # Make the API call
        response = requests.get(self.base_url, params=params)

        date_list = []
        temperature_list = []
        humidity_list = []
        rain_list = []
        sunrise_list = []
        sunset_list = []
        windspeed_list = []
        if response.status_code == 200:
            data = response.json()
            timelines = data.get('data', {}).get('timelines', [])
            for timeline in timelines:
                intervals = timeline.get('intervals', [])
                for interval in intervals:
                    date_list = date_list + [interval.get('startTime')]
                    values = interval.get('values', {})
                    temperature_list = temperature_list + [values.get('temperature')]
                    humidity_list = humidity_list + [values.get('humidity')]
                    rain_list = rain_list + [values.get('rainAccumulation')]
                    sunrise_list = sunrise_list + [values.get('sunriseTime')]
                    sunset_list = sunset_list + [values.get('sunsetTime')]
                    windspeed_list = windspeed_list + [values.get('windSpeed')]
        else:
            print(f"Failed to get data: {response.status_code}, {response.text}")

        forecast_data_df = pd.DataFrame({'action_date': date_list,
                                         'temperature': temperature_list,
                                         'humidity': humidity_list,
                                         'rainAccumulation': rain_list,
                                         'sunriseTime': sunrise_list,
                                         'sunsetTime': sunset_list,
                                         'windSpeed': windspeed_list})
        forecast_data_df['action_date'] = pd.to_datetime(forecast_data_df['action_date'])
        forecast_data_df['time_of_sun'] = pd.to_datetime(forecast_data_df['sunsetTime']) - pd.to_datetime(
            forecast_data_df['sunriseTime'])
        # Convert to hours
        forecast_data_df['time_of_sun'] = forecast_data_df['time_of_sun'].astype(int)/(1000000000*3600)

        return forecast_data_df

    # def load_date_of_interest(self):
    #     # Define the parameters for the API call
    #     print(self.processing_date)
    #     date = self.processing_date
    #     params = {
    #         'location': self.place,  # Latitude and longitude of the location
    #         'fields': ['temperature', 'humidity', 'windSpeed', 'rainIntensity',
    #                    'rainAccumulation', 'sunriseTime', 'sunsetTime'],
    #         'units': 'metric',  # Use 'imperial' for Fahrenheit
    #         'timesteps': '1d',
    #         "startTime": f"{date}T00:00:00Z",  # Start of the specific date in UTC
    #         "endTime": f"{date}T23:59:59Z",
    #         'apikey': self.api_key
    #     }
    #
    #     # Make the API call
    #     response = requests.get(self.base_url, params=params)
    #
    #     date_list = []
    #     temperature_list = []
    #     humidity_list = []
    #     rain_list = []
    #     sunrise_list = []
    #     sunset_list = []
    #     windspeed_list = []
    #     if response.status_code == 200:
    #         data = response.json()
    #         timelines = data.get('data', {}).get('timelines', [])
    #         for timeline in timelines:
    #             intervals = timeline.get('intervals', [])
    #             for interval in intervals:
    #                 date_list = date_list + [interval.get('startTime')]
    #                 values = interval.get('values', {})
    #                 temperature_list = temperature_list + [values.get('temperature')]
    #                 humidity_list = humidity_list + [values.get('humidity')]
    #                 rain_list = rain_list + [values.get('rainAccumulation')]
    #                 sunrise_list = sunrise_list + [values.get('sunriseTime')]
    #                 sunset_list = sunset_list + [values.get('sunsetTime')]
    #                 windspeed_list = windspeed_list + [values.get('windSpeed')]
    #     else:
    #         print(f"Failed to get data: {response.status_code}, {response.text}")
    #
    #     forecast_data_df = pd.DataFrame({'action_date': date_list,
    #                                      'temperature': temperature_list,
    #                                      'humidity': humidity_list,
    #                                      'rainAccumulation': rain_list,
    #                                      'sunriseTime': sunrise_list,
    #                                      'sunsetTime': sunset_list,
    #                                      'windSpeed': windspeed_list})
    #     forecast_data_df['action_date'] = pd.to_datetime(forecast_data_df['action_date'])
    #     forecast_data_df['time_of_sun'] = pd.to_datetime(forecast_data_df['sunsetTime']) - pd.to_datetime(
    #         forecast_data_df['sunriseTime'])
    #     # Convert to hours
    #     forecast_data_df['time_of_sun'] = forecast_data_df['time_of_sun'].astype(int)/(1000000000*3600)
    #
    #     return forecast_data_df
