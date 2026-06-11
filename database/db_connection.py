import mysql.connector
valid_gener=("Fiction","Non-fiction","Science","History","Other")
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root"
)
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS libary_db")
cur.execute("USE libary_db")
conn.commit()
print("database libary_db created successfully")
cur.close()
conn.close()
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
    create_table_books = """CREATE TABLE IF NOT EXISTS books
    (id INT PRIMARY KEY AUTO_INCREMENT ,
    title VARCHAR (50) NOT NULL,
    author ENUM("Fiction","Non-fiction","Science","History","Other")
    ,is_available  BOOLEAN NOT NULL,
    borrowed_by_number_id VARCHAR (50)) """

    cur.execute(create_table_books)
    create_table_members="""CREATE TABLE IF NOT EXISTS members
    (id INT PRIMARY KEY AUTO_INCREMENT ,
    name VARCHAR (50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    is_active BOOLEAN NOT NULL,
    total_borrows INT NOT NULL)"""
    cur.execute(create_table_members)
    conn.commit()
    print("Table 'books,members' created successfully inside 'libary_db'!")
    cur.close()
    conn.close()
create_table()
    
