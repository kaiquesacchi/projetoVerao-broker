from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(debug=False):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)
    api = Api(app)
    define_routes(api)

    # Starts server.
    app.run(debug=debug, host='0.0.0.0', port=5001)


def define_routes(api):
    from .routes.advertisement import Advertisement
    from .routes.discount import Discount
    api.add_resource(Advertisement, '/advertisement')
    api.add_resource(Discount, '/discount')

    # Development only
    from .routes.app_setup import AppSetup
    api.add_resource(AppSetup, '/appsetup')
