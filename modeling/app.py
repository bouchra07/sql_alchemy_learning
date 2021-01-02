from flask import Flask, request
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://docker:docker@localhost:5432/docker"
app.config['SQLALCHEMY_Texport FLASK_APP=app.pyRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



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


if __name__ == '__main__':
    app.run(debug=True)