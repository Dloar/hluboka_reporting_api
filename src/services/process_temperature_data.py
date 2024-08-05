from src.handlers.define_temperature_dictionary_handler import DefineTemperatureDictionaryHandler
from src.queries.data_update.update_raw_temperature_handler import UpdateRawTemperatureHandler


def process_temperature_data(temperature_data):
    weather_data_dict = DefineTemperatureDictionaryHandler(temperature_data=temperature_data).get_weather_data()
    UpdateRawTemperatureHandler(weather_data_dict=weather_data_dict).update_raw_temperature_data()






