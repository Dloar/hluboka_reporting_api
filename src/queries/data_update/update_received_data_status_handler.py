"""
Reporting Back End for Areal Hluboka reporting System
Build 01/08/2024
contact: xkrao11@gmail.com
comment: Status of the calculation

-- Run status
-- 0 Failed
-- 1 Running
-- 2 Finished
-- 4 Status invalid
"""
import datetime
import logging

import pandas as pd

from src.services.create_db_connection import DbConnectorModel


class UpdateReceivedDataStatusHandler:

    def __str__(self):
        return """As we want to keep information about the Income pipeline, we create status table. Each time the process
        is exectuted, we create new calculation id and store the status in the status table. With the process progressing,
        the status is being changed.
        Based on the requirements, we store json in the database so FE can validate numbers that has been sent to the model.  
        """

    def __init__(self, income_data, calculation_id, status=4):
        data = {
            "calculation_id": calculation_id,
            "run_status": status,
            "income_input": str(income_data),
            "action_datetime": datetime.datetime.now()
        }

        self.status_data_df = pd.DataFrame(data=data, index=[0])
        self.update_status_data()

    def update_status_data(self):
        logging.info(f"Logging status data.")
        engine = DbConnectorModel().create_upload_db_connection()

        self.status_data_df.to_sql(name="sup_run_status",
                                   con=engine,
                                   if_exists='append',
                                   index=False)

        logging.info("Status data loaded")

