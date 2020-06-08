from flask import Blueprint, Flask
from flask_restx import Api

from service import cache
from service.config import BaseConfig
from service.api import ns


def create_app(config: BaseConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    cache.init_app(app)

    api_blueprint = Blueprint(__name__, __name__)

    api = Api(api_blueprint)
    api.add_namespace(ns)
    app.register_blueprint(api_blueprint)

    return app


if __name__ == '__main__':
    config = BaseConfig()
    app = create_app(config)

    app.run(debug=True, port=8000)
