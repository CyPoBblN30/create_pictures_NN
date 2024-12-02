import sqlite3


connection = sqlite3.connect('images.db', check_same_thread=False)
sql = connection.cursor()


sql.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, counter INTEGER);')


def register(tg_id):
    sql.execute('INSERT INTO users VALUES (?, ?);', (tg_id, 0))
    connection.commit()


def add_count(tg_id):
    sql.execute('UPDATE users SET counter = counter + 1 WHERE id=?;', (tg_id,))
    connection.commit()


def check_count(tg_id):
    if sql.execute('SELECT counter FROM users WHERE id=?;', (tg_id,)).fetchone():
        return sql.execute('SELECT counter FROM users WHERE id=?;', (tg_id,)).fetchone()[0]
    else:
        return False

