from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
import db

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)


class Compras(Resource):
    def __init__(self):
        self.model = db.Compra()

    def get(self, id=None):
        if request.args.get('date'):
            return self.model.getByDate(str(request.args.get('date')))
        if id is not None:
            return self.model.getById(id)
        if request.args['getAll']:
            print(request.args['getAll'])
            return self.model.getAll()
        return {}, 204

    def post(self):
        body = request.json
        try:
            self.model.insert(body['date'], body['produtos'])
        except IndexError as err:
            return err, 400
        return self.model.getAll()[-1], 201

    def put(self, id):
        try:
            temp = self.model.getById(id)
        except IndexError as err:
            return err, 400
        body = request.json
        self.model.update(id, body['date'], body['produtoId'])
        return self.model.getById(id), 200

    def options(self):
        return ['POST, PUT, DELETE, OPTIONS']

    def delete(self, id):
        temp = None
        try:
            temp = self.model.getById(id)
        except IndexError as err:
            return err, 400
        self.model.delete(id)
        return temp, 200

api.add_resource(Compras, '/api/compras', '/api/compras/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
