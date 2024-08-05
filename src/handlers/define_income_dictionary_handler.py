import datetime
import logging

import numpy as np
import pandas as pd


class DefineIncomeDictionaryHandler:
    def __init__(self, income_data):
        self.income_data = income_data

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
