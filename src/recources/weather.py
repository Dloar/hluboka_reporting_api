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
        try:
            return {"temperature_data": 1}, 201
        except KeyError:
            abort(404, message="Get Weather command failed.")

    @blp.arguments(WeatherSchema)
    @blp.response(201, WeatherSchema)
    def post(self, weather_data):
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
