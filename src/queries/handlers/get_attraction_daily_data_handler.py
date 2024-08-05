# Adwiro 2022
# Load campaign parameters
import logging

import pandas as pd

from src.queries.get_attraction_daily_data_query import GetAttractionDailyDataQuery
from src.services.create_db_connection import DbConnectorModel


class GetAttractionDailyDataHandler:

    @staticmethod
    def load_attraction_daily_data():
        """
        Attraction detail of income data
        :return:
        """
        conn_engine = DbConnectorModel()
        db_conn = conn_engine.create_db_connection()
        attraction_daily_data = pd.read_sql_query(
            GetAttractionDailyDataQuery.query_attraction_daily_data(), db_conn)
        db_conn.close()

        logging.info('Atrakce detail table loaded.')
        return attraction_daily_data
