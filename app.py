"""
Reporting Back End for Areal Hluboka reporting System
Build 01/08/2024
contact: xkrao11@gmail.com
"""
import logging
import os
import warnings

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv

from db import db

from src.recources.income import blp as IncomeBlueprint
from src.recources.weather import blp as WeatherBlueprint


# set up parameters
FORMAT = '%(asctime)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
warnings.filterwarnings("ignore")

def create_app():
    """
    Driver function for the Flask App
    :return:
    """
    app = Flask(__name__)
    load_dotenv()

    # Config Options
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Areal Hluboka Reporting REST API"
    app.config["API_VERSION"] = "v1"
    # smorest will use this for documentation
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"  # os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config['PROPAGATE_EXCEPTION'] = True

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(WeatherBlueprint)
    api.register_blueprint(IncomeBlueprint)

    return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True, host='0.0.0.0', port=8000)
