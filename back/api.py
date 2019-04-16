from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
import db

app = Flask(__name__)
api = Api(app)
CORS(app)

class Produtos(Resource):
    def __init__(self):
        self.model = db.Produto()

    def get(self, id=None):
        return self.model.getAll() if id is None else self.model.getById(id)

    def post(self):
        body = request.json
        try:
            self.model.insert(body['name'], body['price'])
        except IndexError as erro:
            return err, 400
        return self.model.getAll()[-1], 201

    def put(self, id):
        try:
            temp = self.model.getById(id)
        except IndexError as err:
            return err, 400
        body = request.json
        self.model.update(id, body['name'], body['price'])
        return self.model.getById(id), 200

    def delete(self, id):
        temp = None
        try:
            temp = self.model.getById(id)
        except IndexError as err:
            return err, 400
        self.model.delete(id)
        return temp, 200

class Compras(Resource):
    def __init__(self):
        self.model = db.Compra()

    def get(self, id=None):
        if request.args['date']:
            return self.model.getByDate(request.args['date'])
        else:
            return []

    def post(self):
        body = request.json
        try:
            self.model.insert(body['date'], body['produtoId'])
        except IndexError as erro:
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
        return ['GET, POST, PUT, DELETE, OPTIONS']

    def delete(self, id):
        temp = None
        try:
            temp = self.model.getById(id)
        except IndexError as err:
            return err, 400
        self.model.delete(id)
        return temp, 200

api.add_resource(Produtos, '/produtos', '/produtos/<string:id>')
api.add_resource(Compras, '/compras', '/compras/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
