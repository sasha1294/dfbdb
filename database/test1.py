import sqlite3 as sq

def db_start():
    db = sq.connect('data2.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Games(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT);""")
    db.commit()
    return db, cur


db, cur = db_start()

async def sql_add_command_for_games(x):
    cur.execute("""INSERT INTO Games VALUES(NULL, ?);""", (x,))
    db.commit()

async def sql_add_command_for_media(x):
    cur.execute("""INSERT INTO Games VALUES(NULL, ?);""", (x,))
    db.commit()

async def sql_add_command_for_songs(x):
    cur.execute("""INSERT INTO Games VALUES(NULL, ?);""", (x,))
    db.commit()

async def delete():
    sql_delete_query = """DELETE from Games"""
    cur.execute(sql_delete_query)
    db.commit()
    print("Запись успешно удалена")
    db.commit()

def delete_for_start():
    sql_delete_query = """DELETE from Games"""
    cur.execute(sql_delete_query)
    db.commit()
    print("Запись успешно удалена")
    db.commit()