import psycopg2
import numpy as np
import pandas as pd

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

data = pd.read_csv('Code-J.csv')
data = data.drop(data.index[[0]])
cols = data.columns
cols = cols[2:]
X = data[data.columns]
y = data['0Symptoms list']


class Diagnosis(Resource):

    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #     type=float,
    #     required=True,
    #     help="This field cannot be left blank"
    # )


    def get(self):
        # data = Item.parser.parse_args()
        # ip = data

        ip = ['Dining Out', 'Started with spicy meal']

        filtered = data
        for symptom in ip:
            filtered = filtered.loc[((filtered[symptom] == "1") | (filtered[symptom] == "2") )]

        df = filtered.drop_duplicates(subset = ["0Symptoms list"])
        diag = []
        for row in df.itertuples():
            diag.append(row._1)
        
        return {'possibilities': list(diag)}

    
    
    def post(self, name):
        filtered = data['symptoms']
        for symptom in ip:
            filtered = filtered.loc[((filtered[symptom] == "1") | (filtered[symptom] == "2"))]

        df = filtered.drop_duplicates(subset = ["0Symptoms list"])
        diag = []
        for row in df.itertuples():
            diag.append(row._1)
        
        return {'possibilities': list(diag)}


class SymptomList(Resource):
    def get(self):
        return {'items': list(cols)}


api.add_resource(Diagnosis, '/diagnose')
api.add_resource(SymptomList, '/symptoms')

# if __name__ == '__main__':
#     app.run()