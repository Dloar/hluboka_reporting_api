# Adwiro 2022
# Load campaign parameters
import logging

import pandas as pd

from src.queries.get_weather_day_raw_data_query import GetWeatherDayRawDataQuery
from src.services.create_db_connection import DbConnectorModel


class GetWeatherDayRawDataHandler:

    def load_weather_day_raw_data(self):
        """
        Load angles with road.
        :return:
        """
        conn_engine = DbConnectorModel()
        db_conn = conn_engine.create_db_connection()
        day_raw_data = pd.read_sql_query(
            GetWeatherDayRawDataQuery.query_weather_day_raw_data(), db_conn)
        db_conn.close()

        logging.info('Detail den table loaded.')
        return day_raw_data
