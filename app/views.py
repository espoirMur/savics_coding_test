
from model import User, Address, MedicalRecord
from app import app, db
from flask import render_template
from flask import request
from model import User, Address, MedicalRecord


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        data = request.form
        gender_mapping = {'Male': True, 'Female': False}
        address = Address(country=data.get('country'), city=data.get('city'))
        user = User(first_name=data.get('FirstName'), email=data.get('Email'), age=int(data.get('Age')), gender=gender_mapping.get(data.get('gender')))
        user.address = address
        medical_record = MedicalRecord(has_diabetes=bool(data.get('has_diabete')))
        # try:
        db.session.add(address)
        db.session.add(user)
        db.session.add(medical_record)
        db.session.commit()
        """except Exception:
            print(Exception)
            return('an error occurs when saving data')"""
    return render_template("home.html")

