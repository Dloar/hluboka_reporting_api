# Adwiro 2022
# Load campaign parameters
import logging

import pandas as pd


from src.queries.get_weather_day_detail_data_query import GetWeatherDayDetailDataQuery
from src.services.create_db_connection import DbConnectorModel


class GetWeatherDayDetailDataHandler:

    @staticmethod
    def load_weather_day_detail_data():
        """
        Load angles with road.
        :return:
        """
        conn_engine = DbConnectorModel()
        db_conn = conn_engine.create_db_connection()
        den_detail_data = pd.read_sql_query(
            GetWeatherDayDetailDataQuery.query_weather_day_detail_data(), db_conn)
        db_conn.close()

        logging.info('Detail den table loaded.')
        return den_detail_data
