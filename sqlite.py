import sqlite3


def get_db_connection():
    conn = sqlite3.connect("namen.db")
    conn.row_factory = sqlite3.Row  
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS personen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_name(name):
    conn = get_db_connection()
    conn.execute("INSERT INTO personen (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


def get_all_names():
    conn = get_db_connection()
    names = conn.execute("SELECT * FROM personen").fetchall()
    conn.close()

    names_str = ', '.join([name['name'] for name in names])
    print(f'{names[0].keys()=}')
    for k in names[0].keys():
        print(f'{k=}')
        print(f'{k in names[0]=}')
        print(f'{names[0][k]=}')

    return names_str

def del_all_names():
    conn = get_db_connection()
    conn.execute("DELETE FROM personen")
    conn.commit()
    conn.close()

create_table()