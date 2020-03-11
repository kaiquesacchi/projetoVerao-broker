from flask import request
from flask_restful import Resource, reqparse
from ..models.advertisement import ModelAdvertisement
from .. import db


class Advertisement(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'id',
            type=str,
            help='ID of the advertisement'
        )
        args = parser.parse_args(strict=True)
        if not args.id:
            return {"message": "'id' not informed."}, 400

        result = ModelAdvertisement.query.filter_by(id=args.id).first()
        if not result:
            return {"message": "Advertisement not found."}, 404

        return {
            "id": result.id,
            "image": result.image,
            "owner": result.owner,
            "link": result.link
        }

    def post(self):
        body = request.get_json()
        if (body is None or any(map(lambda attribute: attribute not in body, ["image", "owner", "link"]))):
            return {'message': "Request must have body with 'image', 'owner' and 'link'"}, 400

        db.session.add(ModelAdvertisement(body["image"], body["owner"], body["link"]))
        db.session.commit()
        return {'message': 'Created!'}
