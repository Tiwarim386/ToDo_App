from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from marshmallow import ValidationError
db = SQLAlchemy()
marsh = Marshmallow()
import uuid

uuid_entry=str(uuid.uuid4())


class Todo(db.Model):
    #id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    #id = db.Column(uuid_entry, primary_key=True,unique=True)
    id = db.Column(db.Integer, primary_key=True,unique=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(1000))
    assignto = db.Column(db.String(100))
    asdate = db.Column(db.String(100))
    priority = db.Column(db.Integer,default=20)
    complete = db.Column(db.Boolean,default=False)

class TodoSchema(Schema):
    class Meta:
        model=Todo