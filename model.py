from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    age = db.Column(db.Integer(),)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
        nullable=False)

class Address(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    has_diabetes = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
