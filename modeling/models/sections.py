from app import db


class Section(db.Model):
    __tablename__ = 'sections'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String())
    title = db.Column(db.String())

    def __init__(self, number,title):
        self.number = number
        self.title = title

    def __repr__(self):
        return f"<Region {self.title}>"