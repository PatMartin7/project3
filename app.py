from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Troubles_DB"
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def map():
    records = mongo.db.death_record.find()
    return render_template("maps.html", records=records)

@app.route("/visual")
def visuals():
    return render_template("visuals.html")

@app.route("/resources")
def resource():
    return render_template("resources.html")
    


if __name__ == "__main__":
    app.run(debug=True)