import datetime
import logging
import sys

import pandas as pd


class CreateDummyDayHandler:
    def __init__(self, daily_temperature_df):
        self.today = datetime.date.today()
        self.last_date = daily_temperature_df['action_date'].max()

        if self.today == self.last_date:
            logging.info('Date has already been created.')
            sys.exit()
        else:
            self.data_df = self.create_empty_structure()

    def create_empty_structure(self):
        data = {
            "action_date": self.today,
            "temperature": None,
            "humidity": None,
            "wind_speed": None,
            "rain_intensity": None,
            "rain_accumulation": None,
            "time_of_sun": None,
            "day_of_week": self.today.weekday()
        }

        data_df = pd.DataFrame(data, index=[0])

        return data_df