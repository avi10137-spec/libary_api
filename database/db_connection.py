import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="libary_db")
def create_table():
    conn= get_connection()
    cur = conn.cursor()
    create_table_books = """CREATE TABLE IF NOT EXIST books
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR (50) NOT NULL,
    author VARCHAR (50) NOT NULL,
