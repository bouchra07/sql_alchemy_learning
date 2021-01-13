from modeling.models.app import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String())
    name = db.Column(db.String())
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    def __init__(self, code,name,region_id):
        self.code = code
        self.name = name
        self.region_id = region_id
    def __repr__(self):
        return f"<Country {self.name}>"