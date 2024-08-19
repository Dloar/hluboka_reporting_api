import datetime
import logging

import numpy as np
import pandas as pd


class DefineIncomeDictionaryHandler:
    def __init__(self, income_data, source_data):
        self.income_data = income_data
        self.total_employees_number = self.get_total_employees()
        self.calendar_detail_df = source_data.calendar_detail_df
        self.income_dict = self.current_income_data()
        self.attraction_data_df = source_data.attraction_data_df

    def current_income_data(self):
        results_dict = {}
        try:
            for attraction_name in list(self.attraction_data_df['attraction_name']):
                attraction_key = int(
                    self.attraction_data_df.loc[self.attraction_data_df['attraction_name'] == attraction_name][
                        'pk_attraction_dictionary_id'])
                if attraction_name in list(self.income_data.keys()):
                    results_dict[attraction_key] = self.income_data[attraction_name]
                else:
                    results_dict[attraction_key] = 0
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

    def get_total_employees(self):
        if self.income_data['total_employees'].isnull():
            total_employees = None
        else:
            total_employees = self.income_data['total_employees']

        return total_employees




