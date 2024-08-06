import logging

from src.services.create_db_connection import DbConnectorModel


class UpdateDummyTemperaturesHandler:
    def __init__(self, dummy_data_df):
        self.dummy_data_df = dummy_data_df

    def update_dummy_temperatures_data(self):
        logging.info("Logging dummy day data started")
        engine = DbConnectorModel().create_upload_db_connection()
        self.dummy_data_df.to_sql(name="ars_day_temperature",
                                  con=engine,
                                  if_exists='append',
                                  index=False)

        logging.info("Logging dummy day data finished")
