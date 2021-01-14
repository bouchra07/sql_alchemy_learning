from app import db

class CategoryHierarchy(db.Model):
    __tablename__ = 'category_hierarchies'

    ancestor_id = db.Column(db.String(), primary_key=True)
    descendant_id = db.Column(db.String(), primary_key=True)
    generations = db.Column(db.Integer())


    def __init__(self, ancestor_id ,descendant_id,generations):
        self.ancestor_id = ancestor_id
        self.descendant_id = descendant_id
        self.generations = generations

    def __init__(self):
        pass

    def get_descendants(self,id):
        list1 = [i.descendant_id for i in self.query.filter(CategoryHierarchy.ancestor_id == id).all()]
        return list1

    def get_ancestors(self,id):
        return [i.ancestor_id for i in self.query.filter(CategoryHierarchy.descendant_id == id).all()]

