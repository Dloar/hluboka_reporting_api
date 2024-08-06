from typing import NoReturn

from daily_dummy_ingest.handlers.create_dummy_day_handler import CreateDummyDayHandler
from daily_dummy_ingest.handlers.get_all_date_handler import GetAllDataHandler
from src.queries.data_update.update_dummy_temperatures_handler import UpdateDummyTemperaturesHandler


class RunModel:
    def __init__(self):
        pass
    def run_model(self) -> NoReturn:
        daily_temperature_df = GetAllDataHandler().get_daily_temperatures()
        dummy_data_df = CreateDummyDayHandler(daily_temperature_df=daily_temperature_df).create_empty_structure()
        UpdateDummyTemperaturesHandler(dummy_data_df=dummy_data_df).update_dummy_temperatures_data()

