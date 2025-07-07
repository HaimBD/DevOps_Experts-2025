from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)



def get_db_connection():
    r = redis.Redis(host=os.getenv('REDIS_HOST'),
                    port=int(os.getenv('REDIS_PORT')),
                    db=int(os.getenv('REDIS_DB')),
                    username=os.getenv('REDIS_USER'),
                    password=os.getenv('REDIS_PASSWORD'))
    return r

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/add', methods=['POST'])
def add_entry():
    r = get_db_connection()
    r.set('foo', 'bar')
    return jsonify({"status": "success"}), 201

@app.route('/entries', methods=['GET'])
def get_entries():
    r = get_db_connection()
    value = r.get('foo')
    if value is None:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({"foo": value.decode('utf-8')})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)