from os import abort
from flask import Blueprint, request, jsonify
from firebase_admin import  db

MajorApi = Blueprint('major', __name__)
ref = db.reference('/major')

@MajorApi.route('/read/<key>', methods = ['GET'])
def get(key):
    data = ref.child(key).get()
    if data is None: 
        raise ValueError('Key isnt exist')
    return jsonify({'data': data}), 200

@MajorApi.route('/<major_attr>/<major_label>', methods = ['GET'])
def get_skill(major_attr, major_label): 
    data = ref.get()
    majors = list(data.values())
    major_condition = lambda major: major['label'] == major_label
    try: 
        major_obj = list(filter(major_condition, majors))[0]
        skills = major_obj.get(major_attr)
        data = skills
    except Exception as e:
        print(e)
   
    return jsonify({'data': data}), 200