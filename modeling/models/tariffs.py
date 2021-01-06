from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app import db

class Tariff(db.Model):
    __tablename__ = 'tariffs'

    id = db.Column(db.Integer, primary_key=True)
    children = relationship("Child")
    hs_code = db.Column(db.String())
    description = db.Column(db.String())
    chapter = db.Column(db.Integer)
    section_id = db.Column(db.Integer)
    region_id = db.Column(db.Integer)
    parent_id = Column(Integer, ForeignKey('tariffs.id'))

    def __repr__(self):
        return '<Tariff {}>'.format(self.hs_code)


# from app import db
#
# class TariffsModel(db.Model):
#     __tablename__ = 'tariffs'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     hs_code = db.Column(db.String())
#     description = db.Column(db.String())
#     level = db.Column(db.Integer)
#     chapter = db.Column(db.Integer)
#     region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
#     section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=False)
#     parent_id = db.Column(db.Integer(), db.ForeignKey('tariffs.id'))
#     children = db.relationship("Child", back_populates="tariffs")
#
#     def __init__(self, hs_code, description, level, chapter,region_id,section_id,parent_id):
#         self.hs_code = hs_code
#         self.description = description
#         self.level = level
#         self.chapter = chapter
#         self.region_id =region_id
#         self.section_id = section_id
#         self.parent_id = parent_id