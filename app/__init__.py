from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(debug=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    CORS(app)
    db.init_app(app)
    api = Api(app)
    define_routes(api)

    # Starts server.
    app.run(debug=debug, port=6000)


def define_routes(api):
    from .routes.advertisement import Advertisement
    api.add_resource(Advertisement, '/advertisement')

    # Development only
    from .routes.app_setup import AppSetup 
    api.add_resource(AppSetup, '/appsetup')
