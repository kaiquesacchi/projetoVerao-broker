from flask import request
from flask_restful import Resource, reqparse
from .. import db
from ..models.discount import ModelDiscount


class Discount(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'id',
            type=str,
            help='ID of the discount'
        )
        parser.add_argument(
            'owner',
            type=str,
            help='Owner of the advertisement'
        )
        args = parser.parse_args(strict=True)
        if args.id:
            result = ModelDiscount.query.filter_by(id=args.id).first()
        elif args.owner:
            result = ModelDiscount.query.filter_by(owner=args.owner).all()
        else:
            result = ModelDiscount.query.all()

        if not result:
            return {"message": "Discount(s) not found."}, 404

        if type(result) == list:
            return {'discounts': list(map(lambda x: {
                "id": x.id,
                "owner": x.owner,
                "percentage": x.percentage,
                "voucher": x.voucher,
                "text": x.text,
                "link": x.link
            }, result))}
        return {
            "id": result.id,
            "owner": result.owner,
            "percentage": result.percentage,
            "voucher": result.voucher,
            "text": result.text,
            "link": result.link
        }

    def post(self):
        body = request.get_json()
        if (body is None or any(map(lambda attribute: attribute not in body, ["owner", "percentage", "voucher", "text", "link"]))):
            return {'message': "Request must have body with 'owner', 'percentage', 'voucher', 'text', 'link'"}, 400

        db.session.add(ModelDiscount(
            body['owner'], body['percentage'], body['voucher'], body['text'], body['link']))
        db.session.commit()
        return {'message': 'Created!'}
