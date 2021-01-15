from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from tariff_hierarchy import TariffHierarchy

from app import db

class Tariff(db.Model):
    __tablename__ = 'tariffs'

    id = db.Column(db.Integer, primary_key=True)
    hs_code = db.Column(db.String())
    description = db.Column(db.String())
    chapter = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    region_id = db.Column(db.Integer)
    parent_id = Column(Integer, ForeignKey('tariffs.id'))
    children = db.relationship('Tariff', backref=backref('parent', remote_side=[id]))

    def __init__(self, hs_code, description , chapter, region_id, section_id,parent_id):
        self.hs_code = hs_code
        self.description = description
        self.chapter = chapter
        self.region_id = region_id
        self.section_id = section_id
        self.parent_id = parent_id

    def getChildren(self):
        return self.children

    def __init__(self):
        pass

    def getHsCodeBYId(self, id):
        return self.query.filter(Tariff.id == id).first().hs_code

    def getIdByHsCode(self,hs_code):
        return self.query.filter(Tariff.hs_code == hs_code).first().id

    def getDescendantsById(self, id):
        h = TariffHierarchy()
        tree = h.get_descendants(id)
        return [(t, self.getHsCodeBYId(t)) for t in tree]

    def getDescendantsByHsCode(self, hs_code):
        h = TariffHierarchy()
        tree = h.get_descendants(self.getIdByHsCode(hs_code))
        return [(t, self.getHsCodeBYId(t)) for t in tree]

    def getAncestorsById(self,id):
        h = TariffHierarchy()
        tree = h.get_ancestors(id)
        return [(t,self.getHsCodeBYId(t)) for t in tree]

    def getAncestorsByHsCode(self,hs_code):
        h = TariffHierarchy()
        tree = h.get_ancestors(self.getIdByHsCode(hs_code))
        return [(t,self.getHsCodeBYId(t)) for t in tree]










