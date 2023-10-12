from os import abort
from flask import Blueprint, request, jsonify
from firebase_admin import  db

AdmissionApi = Blueprint('admission', __name__)
ref = db.reference('/admission')

@AdmissionApi.route('/documents', methods = ['GET'])
def get():
    data = ref.child('documents').get()
    print(data)
    if data is None: 
        raise ValueError('Key isnt exist')
    return jsonify({'data': data}), 200