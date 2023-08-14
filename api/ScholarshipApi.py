from flask import Blueprint, request, jsonify
from firebase_admin import  db

ScholarshipApi = Blueprint('scholarship', __name__)
scholarshipRef = db.reference('/scholarship')

@ScholarshipApi.route('/read/<key>', methods = ['GET'])
def get(key):
    data = scholarshipRef.child(key).get()
    if data is None: 
        raise ValueError('Value is null')
    return jsonify({'data': data}), 200