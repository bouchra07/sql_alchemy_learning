from app import db

class RegionsModel(db.Model):
    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String())
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"<Region {self.name}>"