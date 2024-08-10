import uuid

from src.handlers.define_income_dictionary_handler import DefineIncomeDictionaryHandler
from src.handlers.get_daily_total_income_handler import GetDailyTotalIncomeHandler
from src.handlers.get_income_data_handler import GetIncomeDataHandler
from src.queries.data_update.update_income_detail_handler import UpdateIncomeDetailHandler
from src.queries.data_update.update_received_data_status_handler import UpdateReceivedDataStatusHandler
from src.queries.data_update.update_results_to_db_handler import UpdateResultsToDb


def process_income_data(income_data,
                        calculation_id=str(uuid.uuid4())
                        ):
    """

    :param income_data:
    :param calculation_id: ID that will represent this calculation in the status table
    :return:
    """

    # Upload status that calculation has been initiated
    UpdateReceivedDataStatusHandler(income_data=income_data, status=0, calculation_id=calculation_id)
    source_data = GetIncomeDataHandler(income_data=income_data)
    structured_income_df = DefineIncomeDictionaryHandler(income_data=income_data,
                                                         source_data=source_data).current_income_final()

    # Update the income by attraction
    UpdateIncomeDetailHandler(structured_income_df)
    source_data = GetDailyTotalIncomeHandler(source_data=source_data, income_data=income_data)

    UpdateResultsToDb(source_data=source_data)
    UpdateReceivedDataStatusHandler(income_data=income_data, status=1, calculation_id=calculation_id)
