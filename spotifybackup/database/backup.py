import os
import sqlite3


def get_last_backup():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''SELECT timestamp FROM backup WHERE id = (SELECT MAX(id) from backup)''').fetchone()
    conn.close()
    return result


def insert_backup():
    conn = sqlite3.connect(os.getenv('DB_PATH'))
    c = conn.cursor()
    result = c.execute('''INSERT INTO backup(timestamp) VALUES (CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()
    return result
