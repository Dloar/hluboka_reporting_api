import uuid

from src.handlers.get_income_data_handler import GetIncomeDataHandler
from src.queries.data_update.update_received_data_status_handler import UpdateReceivedDataStatusHandler


def process_income_data(income_data):
    # Define ID that will represent this calculation in status table
    calculation_id = str(uuid.uuid4())

    # Upload status that calculation has been initiated
    UpdateReceivedDataStatusHandler(income_data=income_data, status=0, calculation_id=calculation_id)

    GetIncomeDataHandler(income_data=income_data).structure_income_data()

    # UpdateReceivedDataStatusHandler(income_data=income_data, status=1, calculation_id=calculation_id)
