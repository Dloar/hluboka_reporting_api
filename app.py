from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from db import db

from src.recources.income import blp as IncomeBlueprint
from src.recources.weather import blp as WeatherBlueprint

def create_app():
    app = Flask(__name__)

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
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" #db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config['PROPAGATE_EXCEPTION'] = True

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(WeatherBlueprint)
    api.register_blueprint(IncomeBlueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8000)