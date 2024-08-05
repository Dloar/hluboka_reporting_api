import datetime
import logging

import numpy as np
import pandas as pd


class DefineIncomeDictionaryHandler:
    def __init__(self, income_data, source_data):
        self.income_data = income_data
        self.calendar_detail_df = source_data.calendar_detail_df
        self.income_dict = self.current_income_data()
    def current_income_data(self):
        results_dict = {}
        try:
            for key in list(range(1, 10)):
                if str(key) in list(self.income_data['daily_income'].keys()):
                    results_dict[key] = self.income_data['daily_income'][str(key)]
                else:
                    results_dict[key] = 0
        except Exception as e:
            logging.info(f'Income data failed to finished with error {e}')

        return results_dict

    def current_income_final(self):
        current_income_df = pd.DataFrame(
            [{"fk_attraction_dictionary_id": t_id, "attraction_income": income} for (t_id, income) in
             self.income_dict.items()])
        current_income_df['action_date'] = self.income_data['action_date']

        # print(self.income_data['action_date'])
        # print(self.calendar_detail_df)
        # temp = self.calendar_detail_df.loc[
        #     self.calendar_detail_df['action_date'] == self.income_data['action_date']]['pk_day_temperature_id']
        # print(temp)
        current_income_df['fk_day_temperature_id'] = 2

        return current_income_df
