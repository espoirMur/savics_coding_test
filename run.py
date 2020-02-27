from flask import Flask
from flask import render_template
from flask import request
from config import database_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")
  
if __name__ == "__main__":
    app.run(debug=True)
