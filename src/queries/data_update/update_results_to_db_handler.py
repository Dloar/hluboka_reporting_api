import datetime
import logging

import pandas as pd

from src.handlers.get_api_weather_report_handler import GetApiWeatherReportHandler
from src.services.create_db_connection import DbConnectorModel


class UpdateResultsToDb:
    def __init__(self, source_data, api_weather_df):
        self.processing_date = source_data.processing_date
        self.temperature_daily_df = pd.DataFrame(source_data.day_temperature,
                                                 index=[0])
        self.total_income_daily_df = pd.DataFrame(source_data.daily_income_total,
                                                  index=[0])
        self.calc_id = self.total_income_daily_df['fk_day_temperature_id'].iloc[0]
        self.update_total_income_daily()
        self.update_temperatures_daily(api_weather_df=api_weather_df.forecast_data_df)

    def update_temperatures_daily(self, api_weather_df):
        selected_forecast_df = api_weather_df.loc[api_weather_df['action_date'].dt.date == self.processing_date]

        temperature = int(selected_forecast_df['temperature'].iloc[0])
        humidity = int(selected_forecast_df['humidity'].iloc[0])
        wind_speed = int(selected_forecast_df['windSpeed'].iloc[0])
        rain_intensity = int(selected_forecast_df['rain_intensity'].iloc[0])
        rain_accumulation = int(selected_forecast_df['rainAccumulation'].iloc[0])
        time_of_sun = int(selected_forecast_df['time_of_sun'].iloc[0])

        # api_temperature = {
        #     "temperature": temperature,
        #     "humidity": humidity,
        #     "wind_speed": wind_speed,
        #     "rain_intensity": rain_intensity,
        #     "rain_accumulation": rain_accumulation,
        #     "time_of_sun": time_of_sun
        # }

        connection = DbConnectorModel().create_db_connection()
        cursor = connection.cursor()
        update_statement = f"""
            UPDATE ars_day_temperature
            SET temperature = {temperature}, humidity = {humidity}, 
                    wind_speed = {wind_speed}, rain_intensity = {rain_intensity},
                     rain_accumulation = {rain_accumulation}, time_of_sun = {time_of_sun} 
            WHERE pk_day_temperature_id = {self.calc_id}
        """
        # Define the values to update and the id of the row to update

        # Execute the update statement
        cursor.execute(update_statement)

        # Commit the transaction to save changes
        connection.commit()

        # Print success message
        print(f"Rows updated: {cursor.rowcount}")

        # Close the connection
        cursor.close()
        connection.close()

    def update_total_income_daily(self):
        logging.info("Income data load started.")
        self.delete_existing_rows()
        # Remove existing lines
        engine = DbConnectorModel().create_upload_db_connection()
        # Update the new data
        self.total_income_daily_df.to_sql(name="ars_daily_income_total",
                                          con=engine,
                                          if_exists='append',
                                          index=False)

        logging.info("Income data load finished.")

    def delete_existing_rows(self):
        connection = DbConnectorModel().create_db_connection()
        # Define your DELETE query
        delete_query = f"DELETE FROM ars_daily_income_total WHERE fk_day_temperature_id = {self.calc_id}"
        cursor = connection.cursor()

        try:
            # Execute the DELETE query
            cursor.execute(delete_query)

            # Commit the changes
            connection.commit()

            print(cursor.rowcount, "record(s) deleted.")
        except Exception as error:
            print(f"Failed to delete record: {error}")
        finally:
            # Close the cursor and connection
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")
