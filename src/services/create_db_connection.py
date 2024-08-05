# Adwiro 2022
# Load database secrets and create connection
import logging

import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine

from src.services.get_config_parameters import ParFactory


class DbConnectorModel:
    def __init__(self):
        config = ParFactory()

        self.host = config.par_factory_var['db_parameters']['host']
        self.user = config.par_factory_var['db_parameters']['username']
        self.passwd = config.par_factory_var['db_parameters']['password']
        self.database = config.par_factory_var['db_parameters']['dbInstanceIdentifier']
        self.port = config.par_factory_var['db_parameters']['port']

    def create_db_connection(self) -> object:
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.database,
                port=self.port
            )
            logging.info("Connection to MySQL DB successful")
        except Error as e:
            logging.info(f"The error '{e}' occurred")

        return conn

    def create_upload_db_connection(self):
        # Create a connection to the database
        connection_string = f"mysql+mysqlconnector://{self.user}:{self.passwd}@{self.host}/{self.database}"
        engine = create_engine(connection_string)

        return engine
