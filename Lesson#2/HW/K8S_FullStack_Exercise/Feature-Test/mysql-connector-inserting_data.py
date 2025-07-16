import mysql.connector
from datetime import *
server = mysql.connector.connect(host="127.0.0.1",
                                 port=3306, user='fullstack-app-user',
                                 password='fullstack-app-password',
                                 database='fullstack_app')

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

