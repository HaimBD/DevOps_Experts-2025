from flask import Flask, request, jsonify
import mysql.connector
from datetime import *
import os

app = Flask(__name__)

def get_db_connection():
    server = mysql.connector.connect(host=os.getenv('MYSQL_HOST'),
                                     port=3306, user=os.getenv('MYSQL_USER'),
                                     password=os.getenv('MYSQL_PASSWORD'),
                                     database=os.getenv('MYSQL_DATABASE'),
                                     auth_plugin=os.getenv('AUTH_PLUGIN'))
    return server

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/add', methods=['POST'])
def add_entry():
    server = get_db_connection()
    cursor = server.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Environment 
        (id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(50), created_at DATETIME
        )
        """)
    cursor.execute("""
        INSERT INTO Environment (type, created_at)
        VALUES (%s, %s)
    """, ("production", datetime.now()))
    server.commit()
    cursor.close()
    server.close()
    return jsonify({"status": "success"}), 201

@app.route('/entries', methods=['GET'])
def get_entries():
    server = get_db_connection()
    cursor = server.cursor()
    cursor.execute("SELECT * FROM Environment")
    entries = cursor.fetchall()
    cursor.close()
    server.close()
    return jsonify(entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)