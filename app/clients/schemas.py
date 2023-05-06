from marshmallow import Schema, fields, validate
from app.clients.models import Clients


class ClientsSchema(Schema):
    class Meta:
        model = Clients

    phone_regex = r'^[+]?[0-9]+$'

    id = fields.Integer(dump_only=True)
    created = fields.DateTime()
    updated = fields.DateTime()
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=64))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=64))
    phone = fields.String(required=True, validate=[validate.Length(min=11, max=20), validate.Regexp(phone_regex, error='Phone number should consist of digits')])
    city = fields.String(required=True, validate=validate.Length(min=1, max=64))




