from marshmallow import Schema, fields, validate
from app.pets.models import Pets


class PetsSchema(Schema):
    class Meta:
        model = Pets

    id = fields.Integer(dump_only=True)
    created = fields.DateTime()
    updated = fields.DateTime()
    petname = fields.String(required=True, validate=validate.Length(min=1, max=64))
    birth_date = fields.Date(format="%Y-%m-%d")
    description = fields.String()
    owner_id = fields.Int()
