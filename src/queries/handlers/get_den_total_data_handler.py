# Adwiro 2022
# Load campaign parameters
import logging

import pandas as pd

from queries.get_den_total_data_query import GetPrijemOverviewDataQuery
from services.create_db_connection import DbConnectorModel


class GetPrijemOverviewDataHandler:

    def load_prijem_overveiew_data(self):
        """
        Load angles with road.
        :return:
        """
        conn_engine = DbConnectorModel()
        db_conn = conn_engine.create_db_connection()
        prijem_overveiew_data = pd.read_sql_query(
            GetPrijemOverviewDataQuery.query_prijem_overveiew_data(), db_conn)
        db_conn.close()

        logging.info('Detail den table loaded.')
        return prijem_overveiew_data
