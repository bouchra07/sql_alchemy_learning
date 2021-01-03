from app import db

class RegionsModel(db.Model):
    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String())
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"<Region {self.name}>"

class CountriesModel(db.Model):
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

class SectionsModel(db.Model):
    __tablename__ = 'sections'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String())
    title = db.Column(db.String())

    def __init__(self, number,title):
        self.number = number
        self.title = title

    def __repr__(self):
        return f"<Region {self.title}>"

class TariffsModel(db.Model):
    __tablename__ = 'tariffs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hs_code = db.Column(db.String())
    description = db.Column(db.String())
    level = db.Column(db.Integer)
    parent = description = db.Column(db.String())
    chapter = db.Column(db.Integer)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=False)

    def __init__(self, hs_code,description,level,parent,chapter,region_id,section_id):
        self.hs_code = hs_code
        self.description = description
        self.level = level
        self.parent = parent
        self.chapter = chapter
        self.region_id = region_id
        self.section_id =section_id
    def __repr__(self):
        return f"<Tariff {self.hs_code}>"


