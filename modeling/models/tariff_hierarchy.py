from sqlalchemy import ForeignKey
from app import db

class TariffHierarchy(db.Model):
    __tablename__ = 'tariff_hierarchies'

    ancestor_id = db.Column(db.Integer(),ForeignKey('tariffs.id'), primary_key=True)
    descendant_id = db.Column(db.Integer(),ForeignKey('tariffs.id'), primary_key=True)
    generation = db.Column(db.Integer())


    def __init__(self, ancestor_id ,descendant_id,generations):
        self.ancestor_id = ancestor_id
        self.descendant_id = descendant_id
        self.generation = generations

    def __init__(self):
        pass

    def get_descendants(self,id):
        list1 = [i.descendant_id for i in self.query.filter(TariffHierarchy.ancestor_id == id).all()]
        return list1

    def get_ancestors(self,id):
        return [i.ancestor_id for i in self.query.filter(TariffHierarchy.descendant_id == id).all()]
