"""
Reporting Back End for Areal Hluboka reporting System
Build 01/08/2024
contact: xkrao11@gmail.com
comment: Function that drives the income data process
"""
import logging

from src.handlers.define_income_dictionary_handler import DefineIncomeDictionaryHandler
from src.handlers.get_api_weather_report_handler import GetApiWeatherReportHandler
from src.handlers.get_daily_total_income_handler import GetDailyTotalIncomeHandler
from src.handlers.get_income_data_handler import GetIncomeDataHandler
from src.queries.data_update.update_income_detail_handler import UpdateIncomeDetailHandler
from src.queries.data_update.update_received_data_status_handler import UpdateReceivedDataStatusHandler
from src.queries.data_update.update_results_to_db_handler import UpdateResultsToDb


def process_income_data(income_data,
                        calculation_id
                        ):
    """

    :param income_data:
    :param calculation_id: ID that will represent this calculation in the status table
    :return:
    """
    try:
        # Upload status that calculation has been initiated
        UpdateReceivedDataStatusHandler(income_data=income_data, status=1, calculation_id=calculation_id)
        source_data = GetIncomeDataHandler(income_data=income_data)
        structured_income_df = DefineIncomeDictionaryHandler(income_data=income_data,
                                                             source_data=source_data).current_income_final()

        # Update the income by attraction
        UpdateIncomeDetailHandler(structured_income_df)
        source_data_total = GetDailyTotalIncomeHandler(source_data=source_data, income_data=income_data)
        api_weather_df = GetApiWeatherReportHandler(processing_date=source_data_total.processing_date)

        UpdateResultsToDb(source_data=source_data, api_weather_df=api_weather_df)
        UpdateReceivedDataStatusHandler(income_data=income_data, status=2, calculation_id=calculation_id)

    except Exception as e:
        logging.info('Status failed')
        UpdateReceivedDataStatusHandler(income_data=income_data, status=0, calculation_id=calculation_id)
        raise e
