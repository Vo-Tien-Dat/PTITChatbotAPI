from firebase_admin import credentials, initialize_app
from flask import Flask


cred = credentials.Certificate("api/key.json")
default_app = initialize_app(cred, {
    'databaseURL': 'https://chatbot-8258a-default-rtdb.firebaseio.com'
})

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CHATBOTFORADMISSIONS'
    from .MajorApi import MajorApi
    from .AdmissionApi import AdmissionApi
    from .CostApi import CostApi

    app.register_blueprint(CostApi, url_prefix = '/cost')
    app.register_blueprint(MajorApi, url_prefix = '/major')
    app.register_blueprint(AdmissionApi, url_prefix = '/admission')
    return app