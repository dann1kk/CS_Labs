import sqlite3
from db_queries import *

conn = sqlite3.connect('dbdata.db', check_same_thread=False)
cursor = conn.cursor()


def create_initial_db_resources():
    cursor.execute(Create_USERS_Table)
    cursor.execute(Create_USER_SECRET_Table)


def create_user(email, password, role):
    cursor.execute(Insert_User, {
        'email': email,
        'password': password,
        'role': role
    })
    print("Created user successfully!")
    conn.commit()


def create_secret(email, totp):
    cursor.execute(Insert_User_Secret, {
        'email': email,
        'totp': totp
    })
    print("Created user secret and inserted successfully!")
    conn.commit()


def get_role(email):
    try:
        cursor.execute(Fetch_User_Role, {
            'email': email
        })
        print("Fetched user role successfully!")
        return cursor.fetchall()
    except Exception as e:
        print("Exception occurred while fetching User's role!")
        raise e


def get_secret(email):
    try:
        cursor.execute(Fetch_User_Secret, {
            'email': email
        })
        print("Fetched user secret successfully!")
        return cursor.fetchall()
    except Exception as e:
        print("Exception occurred while fetching User's TOTP secret!")
        raise e
