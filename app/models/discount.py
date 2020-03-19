from .. import db


class ModelDiscount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String, nullable=False)
    percentage = db.Column(db.Integer, nullable=False)
    voucher = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __init__(self, owner, percentage, voucher, text, link):
        self.owner = owner
        self.percentage = percentage
        self.voucher = voucher
        self.text = text
        self.link = link

    def __repr__(self):
        return f'<Discount ID: [{self.id}] from {self.owner}, link: {self.link}>'
