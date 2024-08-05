import datetime
import threading

from flask import Flask, request, jsonify

from src.services.process_income_data import process_income_data
from src.services.process_temperature_data import process_temperature_data

app = Flask(__name__)

# Create empty dictionary
daily_income = {}
temperature_data = {}

# Daily Income
@app.route("/daily_income", methods=['GET'])
def get_daily_income():
    return {"daily_income": daily_income}


@app.route("/daily_income", methods=['POST'])
def post_income():
    income_response = request.get_json()
    # Append the income data into daily_income dictionary
    daily_income[str(datetime.date.today())] = income_response['daily_income']

    # Create 2 threads One starts with data processing and second one return response
    thread = threading.Thread(target=process_income_data,
                              args=(income_response,))
    thread.start()

    # Return a response immediately
    return jsonify({"status": "Processing started"}), 202

# Temperature
@app.route("/temperature", methods=['GET'])
def get_temperature():
    return {"temperature_data": temperature_data}, 201

@app.route("/temperature", methods=['POST'])
def post_temperature():
    temperature_response = request.get_json()
    # Append the income data into daily_income dictionary
    temperature_data[str(datetime.date.today())] = temperature_response['weather_data']

    # Create 2 threads One start with data processing and second one return response
    thread = threading.Thread(target=process_temperature_data,
                              args=(temperature_response,))
    thread.start()

    # Return a response immediately
    return jsonify({"status": "Processing started"}), 202


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
