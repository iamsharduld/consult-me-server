import psycopg2
import numpy as np
import pandas as pd

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

data = pd.read_csv('https://firebasestorage.googleapis.com/v0/b/consult-me-1447f.appspot.com/o/Code-J.csv?alt=media&token=f237da2e-3eb2-4495-be17-e90ce382eeca')
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

    
    
    def post(self):
        # print(request.get_json())
        req_data = request.get_json()
        print(req_data['symptoms'])
        filtered = data
        for symptom in req_data['symptoms']:
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
#     app.run(debug=True)