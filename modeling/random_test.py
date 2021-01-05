from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://docker:docker@localhost:5432/docker'
sa = SQLAlchemy(app)


class Person(sa.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey('person.id'))
    parent = sa.relationship('Person', uselist=False)
    name = sa.Column(sa.String(80), unique=True)
    def __repr__(self):
        return '<Person:{} child of {}>'.format(self.name, self.parent.name if self.parent else None)

with app.app_context():
    sa.create_all()

with app.test_request_context():
    eve = Person(name="Eve")
    sa.session.add(eve)
    sa.session.commit()

print('Insert:')
for i in range(5):
    with app.test_request_context():
        eve = Person.query.filter_by(name="Eve").first()
        offspring = Person()
        offspring.name = "Foo-{}".format(i)
        offspring.parent = eve
        sa.session.add(offspring)
        sa.session.commit()
        print(offspring)

print()

print('Query:')
for i in range(5):
    with app.test_request_context():
        person = Person.query.filter_by(name="Foo-{}".format(i)).first()
        print(person)