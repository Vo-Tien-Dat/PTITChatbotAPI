from flask import Blueprint, request, jsonify
from firebase_admin import  db

ProgramApi = Blueprint('program', __name__)
programpRef = db.reference('/program')

@ProgramApi.route('/read/<key>', methods = ['GET'])
def get(key):
    data = programpRef.child(key).get()
    if data is None: 
        raise ValueError('Value is null')
    return jsonify({'data': data}), 200