from flask import Flask, render_template, jsonify, request
from flask.json import JSONEncoder
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
import json
from bson import json_util

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Troubles_DB"
mongo = PyMongo(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Nikki789$@localhost/McKeown'
mcsql = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def map():
    records = mongo.db.death_record.find_one()
    print(records)
    return render_template("maps.html")

@app.route("/visual")
def visuals():
    return render_template("visuals.html")

@app.route("/resources")
def resource():
    return render_template("resources.html")

@app.route("/api", methods=['GET', 'POST'])
def api():
    data=mongo.db.death_record.find_one()
    if request.method == 'GET':  
        return json.loads(json_util.dumps(data))
    if request.method == 'POST':
        print(request.get_json())
        return 'Success', 200

@app.route("/apisql")
def apisql():
    return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True)