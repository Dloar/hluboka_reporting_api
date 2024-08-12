import datetime
import logging

import numpy as np
import pandas as pd


class DefineTemperatureDictionaryHandler:
    def __init__(self, temperature_data):
        self.temperature_data = temperature_data

    def get_weather_data(self):
        data = {
            "action_datetime": self.current_action_date(),
            "temperature": self.temperature_handler(),
            "humidity": self.humidity_handler(),
            "wind_speed": self.wind_speed_handler(),
            "rain_intensity": self.rain_intensity_handler(),
            "rain_accumulation": self.rain_accumulation_handler()
        }

        return data

    def current_action_date(self):
        "get current datetime for to ingest"
        try:
            if 'action_date' in list(self.temperature_data.keys()):
                action_datetime = self.temperature_data['action_datetime']
            else:
                action_datetime = str(datetime.datetime.now())
        except Exception as e:
            logging.info(f'Temperature time missing, defined in except part with error {e}')
            action_datetime = str(datetime.datetime.now())

        return action_datetime

    def temperature_handler(self):
        "Get current temperature or define artificial"
        try:
            if 'temperature' in list(self.temperature_data.keys()):
                temperature_value = self.temperature_data['temperature']
            else:
                temperature_value = np.nan
        except Exception as e:
            logging.info(f'Temperature missing, defined in except part with error {e}')
            temperature_value = np.nan

        return temperature_value

    def humidity_handler(self):
        "Get current humidity or define artificial"
        try:
            if 'humidity' in list(self.temperature_data.keys()):
                humidity_value = self.temperature_data['humidity']
            else:
                humidity_value = np.nan
        except Exception as e:
            logging.info(f'Humidity missing, defined in except part with error {e}')
            humidity_value = np.nan

        return humidity_value

    def wind_speed_handler(self):
        "Get current wind speed or define artificial"
        try:
            if 'wind_speed' in list(self.temperature_data.keys()):
                wind_speed_value = self.temperature_data['wind_speed']
            else:
                wind_speed_value = np.nan
        except Exception as e:
            logging.info(f'Wind speed missing, defined in except part with error {e}')
            wind_speed_value = np.nan

        return wind_speed_value

    def rain_intensity_handler(self):
        "Get current rain intensity or define artificial"
        try:
            if 'rain_intensity' in list(self.temperature_data.keys()):
                rain_intensity_value = self.temperature_data['rain_intensity']
            else:
                rain_intensity_value = np.nan
        except Exception as e:
            logging.info(f'Rain Intensity missing, defined in except part with error {e}')
            rain_intensity_value = np.nan

        return rain_intensity_value

    def rain_accumulation_handler(self):
        "Get current rain accumulation or define artificial"
        try:
            if 'rain_accumulation' in list(self.temperature_data.keys()):
                rain_accumulation_value = self.temperature_data['rain_accumulation']
            else:
                rain_accumulation_value = np.nan
        except Exception as e:
            logging.info(f'Rain accumulation missing, defined in except part with error {e}')
            rain_accumulation_value = np.nan

        return rain_accumulation_value

