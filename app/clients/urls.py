from app import db
from app.clients.models import Clients
from app.clients.schemas import ClientsSchema
from app.pets.models import Pets
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError


clients_schema = ClientsSchema(many=True)
client_schema = ClientsSchema()


class ClientsUrls(Resource):
    def get(self):
        clients = Clients.query.all()
        if clients:
            all_clients = clients_schema.dump(clients)
            return {"status": 200, "message": all_clients}, 200
        else:
            return []

    def post(self):
        data = request.json
        try:
            ClientsSchema().load(data)
            client = Clients(first_name=data["first_name"], last_name=data["last_name"], phone=data["phone"], city=data["city"])
            db.session.add(client)
            try:
                db.session.commit()
            except Exception as e:
                if 'clients_phone_key' in str(e):
                    return {"status": 400, "message": 'Repeated value of the phone number'}, 400
            return {"status": 201, "message": "Client created successfully"}, 201
        except ValidationError as err:
            return {"status": 400, "message": err.messages}, 400


class ClientsSearchUrls(Resource):
    def get(self, search_clients):
        clients = Clients.query.filter(Clients.first_name.like('%'+search_clients+'%')).all()
        if clients:
            all_clients = client_schema.dump(clients)
            return {"status": 200, "message": all_clients}, 200
        else:
            return []


class ClientUrls(Resource):
    def get(self, pk: int):
        client = Clients.query.filter_by(id=pk).first()
        if client:
            client_details = client_schema.dump(client)
            return {"status": 200, "message": client_details}, 200
        else:
            return {"status": 404, "message": "Client not available"}, 404

    def put(self, pk):
        client = Clients.query.filter_by(id=pk).first()
        if client:
            data = request.json
            try:
                ClientsSchema().load(data)
                client.first_name = data["first_name"]
                client.last_name = data["last_name"]
                client.phone = data["phone"]
                client.city = data["city"]
                try:
                    db.session.commit()
                except Exception as e:
                    if 'clients_phone_key' in str(e):
                        return {"status": 400, "message": 'Repeated value of the phone number'}, 400
                return {"status": 200, "message": "Client updated successfully"}, 200
            except ValidationError as err:
                return {"status": 400, "message": err.messages}, 400
        else:
            return {"status": 404, "message": "Client not available"}, 404

    def patch(self, pk):
        client = Clients.query.filter_by(id=pk).first()
        if client:
            data = request.json
            try:
                ClientsSchema().load(data, partial=True)
                if 'first_name' in data:
                    client.first_name = data["first_name"]
                if 'last_name' in data:
                    client.last_name = data["last_name"]
                if 'phone' in data:
                    client.phone = data["phone"]
                if 'city' in data:
                    client.city = data["city"]
                try:
                    db.session.commit()
                except Exception as e:
                    if 'clients_phone_key' in str(e):
                        return {"status": 400, "message": 'Repeated value of the phone number'}, 400
                return {"status": 200, "message": "Client updated successfully"}, 200
            except ValidationError as err:
                return {"status": 400, "message": err.messages}, 400
        else:
            return {"status": 404, "message": "Client not available"}, 404

    def delete(self, pk):
        client = Clients.query.filter_by(id=pk).first()
        def has_pet(pk: int) -> bool:
            return False if Pets.query.filter_by(owner_id=pk).first() is None else True
        if client:
            if has_pet(pk):
                return {"status": 409, "message": "Couldn't be deleted - has foreign key constraint"}, 409
            db.session.delete(client)
            db.session.commit()
            return {"status": 204, "message": "Client deleted successfully"}, 204
        else:
            return {"status": 404, "message": "Client not available"}, 404