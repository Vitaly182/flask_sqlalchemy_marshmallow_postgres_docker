from app import db
from app.clients.models import Clients
from app.pets.models import Pets
from app.pets.schemas import PetsSchema
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError


pets_schema = PetsSchema(many=True)
pet_schema = PetsSchema()


class PetsUrls(Resource):
    def get(self):
        pets = Pets.query.all()
        if pets:
            all_pets = pets_schema.dump(pets)
            return {"status": 200, "message": all_pets}, 200
        else:
            return []

    def post(self):
        data = request.json

        def has_client(owner_id: int) -> bool:
            return False if Clients.query.filter_by(id=owner_id).first() is None else True
        if not has_client(data["owner_id"]):
            return {"status": 409, "message": "Couldn't be posted - hasn't foreign key reference"}, 409

        try:
            PetsSchema().load(data)
            pet = Pets(petname=data["petname"])
            if 'birth_date' in data:
                pet.birth_date = data["birth_date"]
            if 'description' in data:
                pet.description = data["description"]
            if 'owner_id' in data:
                pet.owner_id = data["owner_id"]
            db.session.add(pet)
            db.session.commit()
            return {"status": 201, "message": "Pet created successfully"}, 201
        except ValidationError as err:
            return {"status": 400, "message": err.messages}, 400


class PetsSearchUrls(Resource):
    def get(self, search_pets):
        pets = Pets.query.filter(Pets.petname.like('%'+search_pets+'%')).all()
        if pets:
            all_pets = pets_schema.dump(pets)
            return {"status": 200, "message": all_pets}, 200
        else:
            return []


class PetUrls(Resource):
    def get(self, pk: int):
        pet = Pets.query.filter_by(id=pk).first()
        if pet:
            pet_details = pet_schema.dump(pet)
            return {"status": 200, "message": pet_details}, 200
        else:
            return {"status": 404, "message": "Pet not available"}, 404

    def put(self, pk):
        pet = Pets.query.filter_by(id=pk).first()
        if pet:
            data = request.json
            try:
                PetsSchema().load(data)
                if 'petname' in data:
                    pet.petname = data["petname"]
                if 'birth_date' in data:
                    pet.birth_date = data["birth_date"]
                if 'description' in data:
                    pet.description = data["description"]
                if 'owner_id' in data:
                    pet.owner_id = data["owner_id"]
                db.session.commit()
                return {"status": 200, "message": "Pet updated successfully"}, 200
            except ValidationError as err:
                return {"status": 400, "message": err.messages}, 400
        else:
            return {"status": 404, "message": "Pet not available"}, 404

    def patch(self, pk):
        pet = Pets.query.filter_by(id=pk).first()
        if pet:
            data = request.json
            try:
                PetsSchema().load(data)
                if 'petname' in data:
                    pet.petname = data["petname"]
                if 'birth_date' in data:
                    pet.birth_date = data["birth_date"]
                if 'description' in data:
                    pet.description = data["description"]
                if 'owner_id' in data:
                    pet.owner_id = data["owner_id"]
                db.session.commit()
                return {"status": 200, "message": "Pet updated successfully"}, 200
            except ValidationError as err:
                return {"status": 400, "message": err.messages}, 400
        else:
            return {"status": 404, "message": "Pet not available"}, 404

    def delete(self, pk):
        pet = Pets.query.filter_by(id=pk).first()
        if pet:
            db.session.delete(pet)
            db.session.commit()
            return {"status": 204, "message": "Pet deleted successfully"}, 204
        else:
            return {"status": 404, "message": "Pet not available"}, 404