from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://docker:docker@localhost:5432/docker"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import *


@app.route('/')
def hello():
    return {"hello": "world"}


@app.route('/regions', methods=['POST', 'GET'])
def handle_regions():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_region = RegionsModel(name=data['name'])

            db.session.add(new_region)
            db.session.commit()

            return {"message": f"region {new_region.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        regions = RegionsModel.query.all()
        results = [
            {
                "name": region.name
            } for region in regions]

        return {"count": len(results), "regions": results, "message": "success"}


@app.route('/regions/<region_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_region(region_id):
    region = RegionsModel.query.get_or_404(region_id)

    if request.method == 'GET':
        response = {
            "name": region.name
        }
        return {"message": "success", "region": response}

    elif request.method == 'PUT':
        data = request.get_json()
        region.name = data['name']

        db.session.add(region)
        db.session.commit()

        return {"message": f"region {region.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(region)
        db.session.commit()

        return {"message": f"Region {region.name} successfully deleted."}

@app.route('/sections', methods=['POST', 'GET'])
def handle_sections():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_section = SectionsModel(number=data['number'],title=data['title'])

            db.session.add(new_section)
            db.session.commit()

            return {"message": f"section {new_section.title} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        sections = SectionsModel.query.all()
        results = [
            {
                "number": section.number,
                "title": section.title
            } for section in sections]

        return {"count": len(results), "sections": results, "message": "success"}

@app.route('/sections/<section_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_section(section_id):
    section = SectionsModel.query.get_or_404(section_id)

    if request.method == 'GET':
        response = {
            "number": section.number,
            "title": section.title,
        }
        return {"message": "success", "section": response}

    elif request.method == 'PUT':
        data = request.get_json()
        section.number = data['number']
        section.title = data['title']

        db.session.add(section)
        db.session.commit()

        return {"message": f"section {section.title} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(section)
        db.session.commit()

        return {"message": f"section {section.title} successfully deleted."}

@app.route('/countries', methods=['POST', 'GET'])
def handle_countries():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_country = CountriesModel(code=data['code'],name=data['name'],region_id=data['region_id'])

            db.session.add(new_country)
            db.session.commit()

            return {"message": f"country {new_country.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        countries = CountriesModel.query.all()
        results = [
            {
                "code": country.code,
                "name": country.name,
                "region_id": country.region_id
            } for country in countries]

        return {"count": len(results), "countries": results, "message": "success"}

@app.route('/countries/<country_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_country(country_id):
    country = CountriesModel.query.get_or_404(country_id)

    if request.method == 'GET':
        response = {
            "code": country.code,
            "name": country.name,
            "region_id" : country.region_id
        }
        return {"message": "success", "country": response}

    elif request.method == 'PUT':
        data = request.get_json()
        country.code = data['code']
        country.name = data['name']
        country.region_id = data['region_id']

        db.session.add(country)
        db.session.commit()

        return {"message": f"country {country.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(country)
        db.session.commit()

        return {"message": f"country {country.name} successfully deleted."}

@app.route('/tariffs', methods=['POST', 'GET'])
def handle_tariffs():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_tariff = TariffsModel(hs_code=data['hs_code'], description=data['description'],
                                      level=data['level'], parent=data['parent'],
                                      chapter=data['chapter'], region_id=data['region_id'],
                                      section_id=data['section_id'])

            db.session.add(new_tariff)
            db.session.commit()

            return {"message": f"tariff {new_tariff.hs_code} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        tariffs = TariffsModel.query.all()
        results = [
            {
                "hs_code": tariff.hs_code,
                "description": tariff.description,
                "level": tariff.level,
                "parent": tariff.parent,
                "chapter": tariff.chapter,
                "region_id": tariff.region_id,
                "section_id": tariff.section_id
            } for tariff in tariffs]

        return {"count": len(results), "tariffs": results, "message": "success"}

@app.route('/tariffs/<tariff_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_tariff(tariff_id):
    tariff = TariffsModel.query.get_or_404(tariff_id)

    if request.method == 'GET':
        response = {
            "hs_code": tariff.hs_code,
            "description": tariff.description,
            "level": tariff.level,
            "parent": tariff.parent,
            "chapter": tariff.chapter,
            "region_id": tariff.region_id,
            "section_id": tariff.section_id
        }
        return {"message": "success", "tariff": response}

    elif request.method == 'PUT':
        data = request.get_json()
        tariff.hs_code = data['hs_code']
        tariff.description = data['description']
        tariff.level = data['level']
        tariff.chapter = data['chapter']
        tariff.section_id = data['section_id']
        tariff.region_id = data['region_id']

        db.session.add(tariff)
        db.session.commit()

        return {"message": f"tariff {tariff.hs_code} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(tariff)
        db.session.commit()

        return {"message": f"tariff {tariff.hs_code} successfully deleted."}


if __name__ == '__main__':
    app.run(debug=True)