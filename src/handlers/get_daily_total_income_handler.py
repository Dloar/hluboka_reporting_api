from datetime import datetime


class GetDailyTotalIncomeHandler:
    def __init__(self, source_data, income_data):
        self.income_data = income_data
        self.processing_date = datetime.strptime(str(source_data.processing_date), "%Y-%m-%d").date()
        self.calendar_detail_df = source_data.calendar_detail_df
        self.raw_temperature_df = source_data.raw_temperature_df

        daily_income_int, use_id = self.sum_the_daily_income()

        self.daily_income_total = {
            "fk_day_temperature_id": use_id,
            "action_date": source_data.processing_date,
            "total_income": daily_income_int,
            "total_employees": source_data.total_employees_number
        }

        self.day_temperature = {
            "action_date": source_data.processing_date,
            "temperature": self.get_daily_temperature(),
            "humidity": 999,
            "wind_speed": 999,
            "rain_intensity": 999,
            "rain_accumulation": 999,
            "time_of_sun": 999
        }

    def sum_the_daily_income(self):
        calendar_detail_filter_df = self.calendar_detail_df.loc[
            self.calendar_detail_df['action_date'] == self.processing_date]
        daily_income = {key: value for key, value in self.income_data.items() if key != 'action_date'}

        if calendar_detail_filter_df.empty:
            daily_income_int = 999
        else:
            daily_income_int = sum(daily_income.values())

        return daily_income_int, int(calendar_detail_filter_df['pk_day_temperature_id'].iloc[0])

    def get_daily_temperature(self):
        temperature_filter_df = self.raw_temperature_df.loc[
            self.raw_temperature_df['action_datetime'] == self.processing_date]

        if temperature_filter_df.empty:
            daily_temperature_int = 999
        else:
            daily_temperature_int = temperature_filter_df['temperature'].mean()

        return daily_temperature_int
