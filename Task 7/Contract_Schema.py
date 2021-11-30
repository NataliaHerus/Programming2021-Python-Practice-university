from Contract_appear import *
from app import *
from app import db


class Contract(Contract, db.Model):
    __tablename__ = "all_contracts"
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(30), unique=False)
    _email = db.Column(db.String(30), unique=False)
    _phone = db.Column(db.String(13), unique=False)
    _iban = db.Column(db.String(40), unique=False)
    _start_date = db.Column(db.String(10), unique=False)
    _end_date = db.Column(db.String(10), unique=False)

    def __init__(self, **d):
        super().__init__(**d)


class ContractSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone',
                  'iban', 'start_date', 'end_date')
