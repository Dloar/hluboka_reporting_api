# Adwiro 2022
# Load campaign parameters
import logging

import pandas as pd

from src.queries.get_attraction_data_query import GetAttractionDataQuery
from src.services.create_db_connection import DbConnectorModel


class GetAttractionDataHandler:

    def load_attraction_data(self):
        """
        Load angles with road.
        :return:
        """
        conn_engine = DbConnectorModel()
        db_conn = conn_engine.create_db_connection()
        attraction_data = pd.read_sql_query(
            GetAttractionDataQuery().query_attraction_data(), db_conn)
        db_conn.close()

        logging.info('Attraction ids table loaded.')
        return attraction_data
