import psycopg2
import numpy as np

import pandas as pd

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity


googleSheetId = '1dPTIcVN9ux6mX5y8Xql_kvHZXm45mF9UXbdznytyoto'
worksheetName = 'Code-J'
URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
	googleSheetId,
	worksheetName
)

data = pd.read_csv(URL)
cols = data.columns
cols = cols[2:]
X = data[data.columns]
y = data['0Symptoms list']


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
        # data = Item.parser.parse_args()
        # ip = data

        ip = ['Dining Out', 'Started with spicy meal']

        filtered = data
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
        filtered = data
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
        return {'items': list(cols)}


api.add_resource(Diagnosis, '/diagnose')
api.add_resource(SymptomList, '/symptoms')

if __name__ == '__main__':
    app.run(debug=True)