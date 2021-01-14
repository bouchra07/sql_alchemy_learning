from app import db
from category_hierarchy import CategoryHierarchy

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())


    def __init__(self, name):
        self.name = name

    def __init__(self):
        pass

    def getNameBYId(self, id):
        return self.query.filter(Category.id == id).first().name

    def getIdByName(self,name):
        return self.query.filter(Category.name == name).first().id

    def getDescendantsById(self, id):
        h = CategoryHierarchy()
        tree = h.get_descendants(id)
        return [(t, self.getNameBYId(t)) for t in tree]

    def getDescendantsByName(self, name):
        h = CategoryHierarchy()
        tree = h.get_descendants(self.getIdByName(name))
        return [(t, self.getNameBYId(t)) for t in tree]

    def getAncestorsById(self,id):
        h = CategoryHierarchy()
        tree = h.get_ancestors(id)
        return [(t,self.getNameBYId(t)) for t in tree]

    def getAncestorsByName(self,name):
        h = CategoryHierarchy()
        tree = h.get_ancestors(self.getIdByName(name))
        return [(t,self.getNameBYId(t)) for t in tree]