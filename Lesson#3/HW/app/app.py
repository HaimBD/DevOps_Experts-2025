from flask import Flask, request, jsonify
import os

app = Flask(__name__)

APP_ENV = os.getenv('APP_ENV')
LOG_LEVEL = os.getenv('LOG_LEVEL')
DB_PASSWORD = os.getenv('DB_PASSWORD')

@app.route('/')
def hello():
    return f'This app works in the {APP_ENV} environment and logs data on the {LOG_LEVEL} level. The database password is: {DB_PASSWORD}.'

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)