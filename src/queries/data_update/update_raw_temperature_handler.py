import datetime
import logging

import pandas as pd

from src.services.create_db_connection import DbConnectorModel


class UpdateRawTemperatureHandler:
    def __init__(self, weather_data_dict):
        self.weather_data_df = pd.DataFrame(data=weather_data_dict, index=[0])

    def update_raw_temperature_data(self):
        logging.info("Logging raw temperature data started")
        engine = DbConnectorModel().create_upload_db_connection()
        self.weather_data_df.to_sql(name="sup_temperature_raw",
                                    con=engine,
                                    if_exists='append',
                                    index=False)

        logging.info("Logging raw temperature data finished")

