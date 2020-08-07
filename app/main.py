import psycopg2
import numpy as np

import pandas as pd

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from sheets import stomach_data, stomach_data_cols, all_disease_data,  all_disease_data_cols




app = Flask(__name__)
api = Api(app)
cors = CORS(app)
# app.secret_key = 'jose'
# jwt = JWT(app, authenticate, identity)



class Diagnosis(Resource):

    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #     type=float,
    #     required=True,
    #     help="This field cannot be left blank"
    # )
    @cross_origin()
    def get(self):

        ip = ['Dining Out', 'Started with spicy meal']

        filtered = stomach_data
        for symptom in ip:
            filtered = filtered.loc[((filtered[symptom] == 1) | (filtered[symptom] == 2) )]

        df = filtered.drop_duplicates(subset = ["0Symptoms list"])
        diag = []
        for row in df.itertuples():
            diag.append(row._1)
        
        return {'possibilities': list(diag)}

    @cross_origin()
    def post(self):
        # print(request.get_json())
        req_data = request.get_json()
        print(req_data['symptoms'])
        filtered = stomach_data
        for symptom in req_data['symptoms']:
            filtered = filtered.loc[((filtered[symptom] == 1) | (filtered[symptom] == 2))]

        df = filtered.drop_duplicates(subset = ["0Symptoms list"])
        diag = []
        for row in df.itertuples():
            diag.append(row._1)
        
        return {'possibilities': list(diag)}


class SymptomList(Resource):

    @cross_origin()
    def get(self):
        return {'items': list(stomach_data_cols)}


api.add_resource(Diagnosis, '/diagnose')
api.add_resource(SymptomList, '/symptoms')

if __name__ == '__main__':
    app.run(debug=True)