import logging

import pandas as pd
from sqlalchemy import text

from src.services.create_db_connection import DbConnectorModel


class UpdateResultsToDb:
    def __init__(self, source_data):
        self.temperature_daily_df = pd.DataFrame(source_data.day_temperature,
                                                 index=[0])

        self.total_income_daily_df = pd.DataFrame(source_data.daily_income_total,
                                                  index=[0])

        self.update_total_income_daily()
    def update_temperatures_daily(self):
        pass


    def update_total_income_daily(self):
        logging.info("Income data load started.")
        # Remove existing lines
        engine = DbConnectorModel().create_upload_db_connection()
        # Define your DELETE statement
        delete_statement = text(
            f"DELETE FROM ars_daily_income_total WHERE fk_day_temperature_id = 4")
        print(delete_statement)
        # Execute the DELETE statement
        with engine.connect() as connection:
            connection.execute(delete_statement)

        # Update the new data
        self.total_income_daily_df.to_sql(name="ars_daily_income_total",
                                          con=engine,
                                          if_exists='append',
                                          index=False)

        logging.info("Income data load finished.")