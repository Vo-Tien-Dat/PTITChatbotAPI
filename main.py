from api import create_app
import os
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

slack_token = os.getenv("SLACK_API_TOKEN")
debug_mode = os.getenv("DEBUG_MODE")
port = os.getenv("PORT")
app = create_app()

@app.errorhandler(Exception)
def handle_global_exceptions(error):
    error_message = str(error)
    response = jsonify({'error': error_message})
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run(debug=debug_mode, port=port)