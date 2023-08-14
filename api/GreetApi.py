from flask import Blueprint, request, jsonify
from firebase_admin import  db

GreetApi = Blueprint('greet', __name__)
ref = db.reference('/greet')

@GreetApi.route('/read/<key>', methods = ['GET'])
def get(key):
    try:
        data = ref.child(key).get()
        if data is None: 
            raise ValueError('Key isnt exist')
        return jsonify({'data': 'hello'}), 200
    except Exception as e: 
        return f"Error: {e}"