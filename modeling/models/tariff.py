from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from modeling.models.app import db

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

    # def getChildren(self):
    #     return self.children
    #
    # def get_tree(self):
    #     if self.children == []:
    #         return
    #     else:
    #         print(self.children)
    #         for child in self.children:
    #             child.get_tree()
    j=0
    def get_tree(self):
        for i in self.children:

            print(self.j*'-' + i.description)
            i.get_tree()





