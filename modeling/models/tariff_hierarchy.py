from app import db

class CategoryHierarchy(db.Model):
    __tablename__ = 'category_hierarchies'

    ancestor_id = db.Column(db.String(), primary_key=True)
    descendant_id = db.Column(db.String(), primary_key=True)
    generation = db.Column(db.Integer())


    def __init__(self, ancestor_id ,descendant_id,generations):
        self.ancestor_id = ancestor_id
        self.descendant_id = descendant_id
        self.generation = generations
