from src.handlers.define_temperature_dictionary_handler import DefineTemperatureDictionaryHandler
from src.queries.data_update.update_raw_temperature_handler import UpdateRawTemperatureHandler


def process_temperature_data(temperature_data):
    """
    The Temperature pipeline is very straight forward. As we are collecting data from meteo station in Areal, we
    need to ingest the data. As this pipeline is activated, it takes input from meteo station and store it the database.
    We should receive four readings every day.
    :param temperature_data: json format with weather information and datetime
    :return:
    """
    weather_data_dict = DefineTemperatureDictionaryHandler(temperature_data=temperature_data).get_weather_data()
    UpdateRawTemperatureHandler(weather_data_dict=weather_data_dict).update_raw_temperature_data()






