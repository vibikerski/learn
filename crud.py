import sqlite3
import os

def start_table(con, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255),
        email VARCHAR(255)
    )
    """)
    con.commit()


def add_user(con, cursor, username, email):
    params = (username, email)
    cursor.execute("""
    INSERT INTO users (username, email)
    VALUES
    (?, ?)
    """, params)
    con.commit()
    user = {
        "id": cursor.lastrowid,
        "username": username,
        "email": email
    }
    return user


def get_user(cursor, id):
    params = id,

    user = cursor.execute("""
    SELECT id, username, email
    FROM users
    WHERE id = ?
    LIMIT 1
    """, params).fetchone()

    return {
        "id": user[0],
        "username": user[1],
        "email": user[2]
    }

def get_all_users(cursor):
    result = cursor.execute("""
    SELECT id, username, email
    FROM users
    """)

    user_list = []

    user = result.fetchone()
    while user:
        processed_user = {
            "id": user[0],
            "username": user[1],
            "email": user[2]
        }
        
        user_list.append(processed_user)
        user = result.fetchone()

    return user_list

PATH = os.path.dirname(__file__) + os.sep

con = sqlite3.connect(PATH + 'students.db')
cursor = con.cursor()

start_table(con, cursor)
