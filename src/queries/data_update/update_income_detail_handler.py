import datetime
import logging

import pandas as pd

from src.services.create_db_connection import DbConnectorModel


class UpdateIncomeDetailHandler:
    def __init__(self, structured_income_df, source_data):
        self.structured_income_df = structured_income_df
        self.income_detail_df = source_data.daily_income_df
        self.day_temp_id = int(self.structured_income_df['fk_day_temperature_id'].unique())

        # Functions
        self.update_income_detail_data()

    def update_income_detail_data(self):
        if self.day_temp_id in list(self.income_detail_df['fk_day_temperature_id'].unique()):
            self.delete_old_rows()

        logging.info("Logging raw temperature data started")
        engine = DbConnectorModel().create_upload_db_connection()
        self.structured_income_df.to_sql(name="ars_daily_income_detail",
                                         con=engine,
                                         if_exists='append',
                                         index=False)

        logging.info("Logging income detail data finished")

    def delete_old_rows(self):
        connection = DbConnectorModel().create_db_connection()
        # Define your DELETE query
        delete_query = f"DELETE FROM ars_daily_income_detail WHERE fk_day_temperature_id = {self.day_temp_id}"
        cursor = connection.cursor()
        try:
            # Execute the DELETE query
            cursor.execute(delete_query)

            # Commit the changes
            connection.commit()

            print(cursor.rowcount, "record(s) deleted.")
        except Exception as error:
            print(f"Failed to delete record: {error}")
        finally:
            # Close the cursor and connection
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")