import sqlite3
from multiprocessing import connection
from tkinter.constants import INSERT


def create_table():
    connection =sqlite3.connect('./myidatabase.db')
    cursor = connection.cursor()
    sql ="""CREATE TABLE IF NOT EXISTS user(
        user_id INTEGER PRIMARY KEY ,
        username VARCHAR(200) ,
        password VARCHAR(60)
        );
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()

create_table()

def add_to_database(username=None,password=None):
    connection=sqlite3.connect('./myidatabase.db')
    cursor=connection.cursor()
    cursor.execute("""
    INSERT INTO user (username , password) VALUES 
    (? ,?)""" ,(username,password))
    connection.commit()
    return "success"
    connection.close()


def select_from_db():
    connection=sqlite3.connect('./myidatabase.db')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM user")
    res = cursor.fetchall()
    connection.commit()
    connection.close()


def update_db():
    connection=sqlite3.connect('./myidatabase.db')
    cursor=connection.cursor()
    sql = """
        UPDATE user SET username = ? where password = ?
        """
    cursor.execute(sql)
    connection.commit()
    connection.close()

def delete_from_db():
    connection=sqlite3.connect('./myidatabase.db')
    cursor=connection.cursor()
    sql = """
    DELETE FROM user WHERE username = ?;
            """
    cursor.execute(sql)
    connection.commit()
    connection.close()

def select_from_db_user(username):
    connection=sqlite3.connect('./myidatabase.db')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM user WHERE username = ?" ,(username,))
    res = cursor.fetchone()
    connection.commit()
    connection.close()
    return res