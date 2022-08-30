from lib.db import get_database

def get_message():
    db = get_database()
    return db[0]