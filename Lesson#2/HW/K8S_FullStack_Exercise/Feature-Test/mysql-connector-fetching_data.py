import mysql.connector

server = mysql.connector.Connect(host="127.0.0.1", port=3306, user="fullstack-app-user", password="fullstack-app-password", database='fullstack_app')

cursor = server.cursor()

cursor.execute("SELECT * FROM Environment")

row = cursor.fetchall()

print(row)

