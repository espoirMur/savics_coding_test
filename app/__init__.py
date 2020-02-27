from flask import Flask
from config import database_file
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

from app import views
