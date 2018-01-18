from flask import Flask,redirect,render_template,request,flash,session,jsonify
from flask_bootstrap import Bootstrap

import json
import requests
mongo_user = "python"
mongo_pass = "12345"
mongo_DB="car_models"
from flask_pymongo  import PyMongo
app =Flask(__name__)
app.config['MONGO_DBNAME']= mongo_DB
app.config['MONGO_URI'] = 'mongodb://'+mongo_user+":"+mongo_pass+"@ds255767.mlab.com:55767/car_models"
Bootstrap(app)
with app.app_context():
    mongo = PyMongo(app)

myCollection =requests.get("https://api.mlab.com/api/1/databases/car_models/collections/cars?apiKey=",
)
@app.route('/find/<string:car_make>/<string:car_model>',methods=["GET"])
def find_car(car_make,car_model):
    cars = mongo.db.cars
    for car in cars.find():
        print(car["make"][car_make])
    return 'your Car is a '+car_make+" "+car["make"][car_make]['models'][car_model]["category"]

@app.route('/find',methods=["GET"])
def find_car_type():
    cars = mongo.db.cars
    if not request.json:
        return "make a request /find/car-make/car-model"
    return "No access to the server"

if __name__ == '__main__':
    app.run(debug=True)
