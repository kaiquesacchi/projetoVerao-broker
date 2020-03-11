from flask import request
from flask_restful import Resource
from .. import db


class AppSetup(Resource):
    def get(self):
        return {"message": "Broker working."}
    
    def post(self):
        db.create_all()
        return {"message": "Database created."}