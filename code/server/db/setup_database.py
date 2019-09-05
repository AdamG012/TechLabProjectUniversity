import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="pass"
)

db_cursor = db.cursor()
db_cursor.execute("SHOW DATABASES")

try:
    db_cursor.execute("CREATE DATABASE trends_database")
except mysql.connector.errors.DatabaseError:
    pass
db.close()


db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="pass",
    database="trends_database"
)

db_cursor = db.cursor()
# TODO: set max body length
db_cursor.execute("CREATE TABLE articles (id INT PRIMARY KEY, title VARCHAR(255), "
                  "author VARCHAR(255), abstract VARCHAR(255), "
                  "body VARCHAR(X), date DATE, time_to_read INT")

db.close()
