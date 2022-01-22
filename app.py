from flask import Flask, render_template, jsonify, request
from flask.json import JSONEncoder
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
import json
import psycopg2
from bson import json_util
from queries import *

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Troubles_DB"
mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/visual")
def visuals():
    return render_template("visuals.html")

@app.route("/resources")
def resource():
    return render_template("resources.html")

@app.route("/api", methods=['GET', 'POST'])
def api():
    somestuff=[doc for doc in mongo.db.death_record.find()]
    data = {"Mongo": somestuff}
    if request.method == 'GET':  
        return json.loads(json_util.dumps(data))
    if request.method == 'POST':
        print(request.get_json())
        return 'Success', 200

@app.route('/api2', methods=['GET', 'POST'])
def api2fn():
    # SQL Function
    sqllist = sqlsearch(sqlbyyear)
    # GET request
    if request.method == 'GET':
        message = sqllist
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.route('/api3', methods=['GET', 'POST'])
def api3fn():
    # SQL Function
    sqllist = sqlsearch(sqlbygender)
    # GET request
    if request.method == 'GET':
        message = sqllist
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.route('/api4', methods=['GET', 'POST'])
def api4fn():
    # SQL Function
    sqllist = sqlsearch(sqlbyagency)
    # GET request
    if request.method == 'GET':
        message = sqllist
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.route('/api5', methods=['GET', 'POST'])
def api5fn():
    # SQL Function
    sqllist = sqlsearch(sqlbycontext)
    # GET request
    if request.method == 'GET':
        message = sqllist
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.route("/charts")
def apisql():
    return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True)