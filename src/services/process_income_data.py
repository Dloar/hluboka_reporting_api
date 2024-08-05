import uuid

from src.handlers.define_income_dictionary_handler import DefineIncomeDictionaryHandler
from src.handlers.get_income_data_handler import GetIncomeDataHandler
from src.queries.data_update.update_income_detail_handler import UpdateIncomeDetailHandler
from src.queries.data_update.update_received_data_status_handler import UpdateReceivedDataStatusHandler


def process_income_data(income_data):
    # Define ID that will represent this calculation in status table
    calculation_id = str(uuid.uuid4())

    # Upload status that calculation has been initiated
    UpdateReceivedDataStatusHandler(income_data=income_data, status=0, calculation_id=calculation_id)
    source_data = GetIncomeDataHandler(income_data=income_data)
    structured_income_df = DefineIncomeDictionaryHandler(income_data=income_data,
                                                           source_data=source_data).current_income_final()

    UpdateIncomeDetailHandler(structured_income_df)
    # UpdateReceivedDataStatusHandler(income_data=income_data, status=1, calculation_id=calculation_id)
