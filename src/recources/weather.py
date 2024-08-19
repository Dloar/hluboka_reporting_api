"""
Reporting Back End for Areal Hluboka reporting System
Build 01/08/2024
contact: xkrao11@gmail.com
comment: Application has three main targets and we have two REST API endpoints.
This is a Weather recourse; that has simple purpose of bringing the temperatures from
local meteo station in the database.
"""

import threading

from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import WeatherSchema
from src.services.process_temperature_data import process_temperature_data

blp = Blueprint("weather", __name__, description="Ingestion of weather readings.")

@blp.route("/weather")
class Weather(MethodView):
    @blp.response(200)
    def get(self):
        # TODO: In this load, we could load the raw data and return the latest loaded data
        try:
            return {"temperature_data": 'Weather pipeline alive'}, 200
        except KeyError:
            abort(404, message="Get Weather command failed.")

    @blp.arguments(WeatherSchema)
    @blp.response(201, WeatherSchema)
    def post(self, weather_data):
        """
        The Reason for creating multiple threads is to take care of calculation within the API, but return
        the status quickly after the call starts.
        :param weather_data: Define a json format to send into API.
        :return:
        """
        try:
            # Create 2 threads: one to start data processing and the second to return response
            thread = threading.Thread(target=process_temperature_data, args=(weather_data,))
            thread.start()

            # Return a response immediately with the action date being processed
            return jsonify({
                "status": "Processing started",
                "action_date": weather_data['action_datetime']
            }), 202
        except KeyError:
            abort(404, message="Post Weather command failed.")
