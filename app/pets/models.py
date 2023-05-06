from datetime import datetime
from .. import db # from __init__.py



class Pets(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    petname = db.Column(db.String(64), nullable=False)
    birth_date = db.Column(db.Date)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('clients.id'))