from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/matchmaking_db"
app.config['JSON_SORT_KEYS'] = False
mongo = PyMongo(app)   



