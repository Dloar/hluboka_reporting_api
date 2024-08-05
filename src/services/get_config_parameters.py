# Adwiro 2022
# Load config file from S3 Bucket
import os
from typing import Dict

import yaml


class ParFactory:
    def __init__(self):
        """

        :rtype: object
        """
        # Load a YAML file
        with open('configs/config.yaml', 'r') as file:
            self.par_factory_var = yaml.safe_load(file)
