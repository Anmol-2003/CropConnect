from flask import Flask, request, jsonify, current_app
from flask_restful import Api, Resource
import torch
import torch.nn as nn 
import requests
import pandas as pd 
import numpy as np 
from PIL import Image
import json 
from pymongo.mongo_client import MongoClient
import urllib.parse
import matplotlib.pyplot as plt


# DATABASE CONNECTION - 
# username = urllib.parse.quote_plus('aikimkc14')
# password = urllib.parse.quote_plus('MJTDEHRLLjM5InI9')

client=MongoClient("mongodb://localhost:27017")
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['CropConnect']
users_collection = db['Users']
verified_claims = db['Verified_Claims']


class Users(Resource):
    def get(self):
        data = request.get_json()
        print(data)
        return "Success", 200
    def post(self):
        data = request.get_json()
        users_collection.insert_one(data)
        return "User Resgistered", 201
    
class Verify(Resource):
    def get(self):
        data = request.get_json()
        print(data)
        return "Success", 200
    def post(self):
        data = request.get_json()
        image = data['image']
    # ----
        # model inference here 
    # ----

        return "Success" , 201

def server():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Users, "/register")
    api.add_resource(Verify, "/claimInsurance")

    return app 


if __name__ == "__main__":
    app = server()
    app.run(debug = True)



