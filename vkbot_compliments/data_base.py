import sqlite3
from random import randint

global db, sql

db = sqlite3.connect('data.db')
sql = db.cursor()


def get_data():
    sql_select_compliment = """SELECT compliment FROM compliments"""
    sql.execute(sql_select_compliment)
    all_compliments = sql.fetchall()
    i = randint(0, len(all_compliments))
    return all_compliments[i]




