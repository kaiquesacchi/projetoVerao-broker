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
        parser.add_argument(
            'owner',
            type=str,
            help='Owner of the advertisement'
        )
        args = parser.parse_args(strict=True)
        if args.id:
            result = ModelAdvertisement.query.filter_by(id=args.id).first()
        elif args.owner:
            result = ModelAdvertisement.query.filter_by(owner=args.owner).all()
        else:
            result = ModelAdvertisement.query.all()

        if not result:
            return {"message": "Advertisement(s) not found."}, 404

        if type(result) == list:
            return {'advertisements': list(map(lambda x: {
                "id": x.id,
                "image": x.image,
                "owner": x.owner,
                "link": x.link
            }, result))}
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

        db.session.add(ModelAdvertisement(
            body["image"], body["owner"], body["link"]))
        db.session.commit()
        return {'message': 'Created!'}
