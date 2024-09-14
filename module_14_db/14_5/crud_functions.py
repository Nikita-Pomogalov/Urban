import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)
    connection.commit()
    connection.close()

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))
    connection.commit()

def is_included(username):
    cursor.execute('SELECT EXISTS(SELECT 1 FROM Users WHERE username=?)', (username, ))
    exists = cursor.fetchone()[0]
    return bool(exists)

def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products