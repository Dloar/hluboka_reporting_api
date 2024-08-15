import datetime
import threading

from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import IncomeSchema
from src.services.process_income_data import process_income_data

blp = Blueprint("income", __name__, description="Uploading the daily income.")

@blp.route("/daily_income")
class Income(MethodView):

    @blp.response(200)
    def get(self):
        try:
            return {"daily_income": 'Income pipeline alive'}, 201
        except KeyError:
            abort(404, message="Get Income command failed.")
    @blp.arguments(IncomeSchema)
    @blp.response(201, IncomeSchema)
    def post(self, income_data):
        try:
            # Create 2 threads: one to start data processing and the second to return a response
            thread = threading.Thread(target=process_income_data, args=(income_data,))
            thread.start()

            # Return a response immediately with the action date being processed
            return jsonify({
                "action_date": income_data['action_date']
            }), 202
        except KeyError:
            abort(404, message="Post Income command failed.")
