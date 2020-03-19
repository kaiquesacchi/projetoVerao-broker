from .. import db


class ModelAdvertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text, nullable=False)
    owner = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __init__(self, image, owner, link):
        self.image = image
        self.owner = owner
        self.link = link

    def __repr__(self):
        return f'<Advertisement ID: [{self.id}] from {self.owner}, link: {self.link}>'
