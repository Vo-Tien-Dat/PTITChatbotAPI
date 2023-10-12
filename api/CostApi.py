from os import abort
from flask import Blueprint, request, jsonify
from firebase_admin import  db

CostApi = Blueprint('cost', __name__)
ref = db.reference('/cost')

@CostApi.route('/documents', methods = ['GET'])
def get():
    data = ref.child('documents').get()
    print(data)
    if data is None: 
        raise ValueError('Key isnt exist')
    return jsonify({'data': data}), 200

@CostApi.route('/methods', methods = ['GET'])
def get_methods():
    data = ref.child('methods').get()

    if data is None: 
        raise ValueError('Key isnt exist')
    return jsonify({'data': data}), 200

@CostApi.route('/scholarship/<scholarship_name>', methods = ['GET'])
def get_scholarship(scholarship_name):
    data = ref.child('scholarships').get()
    data = [scholarship for scholarship in data.values() if scholarship.get('name') == scholarship_name]

    if data is None: 
        raise ValueError('Key isnt exist')
    return jsonify({'data': data}), 200

@CostApi.route('/scholarship/<scholarship_name>/<scholarship_field>', methods = ['GET'])
def get_scholarship_field(scholarship_name, scholarship_field):
    data = ref.child('scholarships').get()
    data = [scholarship for scholarship in data.values() if scholarship.get('name') == scholarship_name]
    data = data[0].get(scholarship_field)
    if data is None: 
        raise ValueError('Key isnt exist')
    return jsonify({'data': data}), 200
