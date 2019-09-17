from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Items(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': 'item not found'}, 404
    
    def post(self, name):
        item = {'name': name, 'price': 12.00}  
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Items, '/items/<string:name>')
api.add_resource(ItemList, 'items')

app.run(port=5000, debug=True)
