from os import abort
from flask import Blueprint, request, jsonify
from firebase_admin import  db

MajorApi = Blueprint('major', __name__)
ref = db.reference('/major')

@MajorApi.route('/read/<key>', methods = ['GET'])
def get(key):
    print('hello')
    data = ref.child(key).get()
    print(data)
    if data is None: 
        raise ValueError('Key isnt exist')
    return jsonify({'data': data}), 200
    