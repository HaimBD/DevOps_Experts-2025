# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/service1')
def service1():
    return "This is Service 1!"

@app.route('/service2')
def service2():
    return "This is Service 2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
