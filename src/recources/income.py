"""
Reporting Back End for Areal Hluboka reporting System
Build 01/08/2024
contact: xkrao11@gmail.com
comment: Application has three main targets, and we have two REST API endpoints.
Here we have a challenging process, that is bringing daily income.
This is being sent by dashboard, and it is filled by each attraction. Currently, we have nine valid attractions.
Every day, someone needs to input the income we save it in the source db.
This API is also trigger for other actions. We calculate total daily income and fill the final daily weathert information
form raw.
"""

import threading
import uuid

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
        # TODO: Can be returning last total date and income inserted.
        try:
            return {"daily_income": 'Income pipeline alive'}, 201
        except KeyError:
            abort(404, message="Get Income command failed.")
    @blp.arguments(IncomeSchema)
    @blp.response(201, IncomeSchema)
    def post(self, income_data):
        try:
            calculation_id = str(uuid.uuid4())
            # Create 2 threads: one to start data processing and the second to return a response
            thread = threading.Thread(target=process_income_data, args=(income_data, calculation_id, ))
            thread.start()

            # Return a response immediately with the action date being processed
            return jsonify({
                "action_date": income_data['action_date'],
                "calculation_id": calculation_id
            }), 201
        except KeyError:
            abort(404, message="Post Income command failed.")
