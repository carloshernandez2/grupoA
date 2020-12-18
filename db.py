import sqlite3
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
def get_db():
    con = sqlite3.connect("cafeteria1.db")
    con.row_factory = dict_factory
    return con
def close_db(con):
    con.close()