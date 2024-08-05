import datetime
import logging

import pandas as pd

from src.services.create_db_connection import DbConnectorModel


class UpdateIncomeDetailHandler:
    def __init__(self, structured_income_df):
        self.structured_income_df = structured_income_df
        self.update_income_detail_data()

    def update_income_detail_data(self):
        logging.info("Logging raw temperature data started")
        engine = DbConnectorModel().create_upload_db_connection()
        self.structured_income_df.to_sql(name="ars_daily_income_detail",
                                         con=engine,
                                         if_exists='append',
                                         index=False)

        logging.info("Logging income detail data finished")
