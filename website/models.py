from . import db
from sqlalchemy.sql import func

class PersonalComputer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset = db.Column(db.String(20), unique=True)
    sn = db.Column(db.String(20), unique=True)
    user = db.Column(db.String(50))
    date = db.Column(db.String(20))

class Phone(db.Model):
    asset = db.Column(db.String(20), primary_key=True)
    sn = db.Column(db.String(20), unique=True)
    user = db.Column(db.String(50))
    date = db.Column(db.String(20))
    phone = db.Column(db.BigInteger)

class Printer(db.Model):
    asset = db.Column(db.String(20), primary_key=True)
    sn = db.Column(db.String(20), unique=True)
    user = db.Column(db.String(50))
    date = db.Column(db.String(20))
    ipaddress = db.Column(db.BigInteger)
    location = db.Column(db.String(150))
    printer = db.Column(db.String(30))