
from model import User, Address, MedicalRecord
from app import app, db
from flask import render_template
from flask import request
from model import User, Address, MedicalRecord


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form and request.method=='POST':
        data = request.form
        gender_mapping = {'Male': True, 'Female': False}
        address = Address(country=data.get('country'), city=data.get('city'))
        user = User(
            first_name=data.get('FirstName'),
            last_name=data.get('LastName'),
            email=data.get('Email'),
            age=int(
                data.get('Age')),
            gender=gender_mapping.get(
                data.get('gender')))
        user.address = address
        medical_record = MedicalRecord(
            has_diabetes=bool(
                data.get('has_diabete')))
        medical_record.user = user
        try:
            db.session.add(address)
            db.session.add(user)
            db.session.add(medical_record)
            db.session.commit()
        except Exception as exc:
            print(exc.__traceback__, '')
            return('an error occurs when saving data')
    elif request.method=='GET':
        records = MedicalRecord.query.all()
        for record in records:
            print(record.user.first_name, '=====>')
        return render_template("home.html", records=records)
    return render_template("home.html")
