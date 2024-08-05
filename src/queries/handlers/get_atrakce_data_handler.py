# Adwiro 2022
# Load campaign parameters
import logging

import pandas as pd

from queries.get_atrakce_data_query import GetAtrakceDataQuery
from services.create_db_connection import DbConnectorModel


class GetAtrakceDataHandler:

    def load_atrakce_data(self):
        """
        Load angles with road.
        :return:
        """
        conn_engine = DbConnectorModel()
        db_conn = conn_engine.create_db_connection()
        atrakce_data = pd.read_sql_query(
            GetAtrakceDataQuery.query_atrakce_data(), db_conn)
        db_conn.close()

        logging.info('Atrakce ids table loaded.')
        return atrakce_data
