try:
    import requests
    import sqlite3
    from sqlite3 import Error
    from getmac import get_mac_address as gma
except Exception:
    pass

user_system = ""

def create_connection(db_file):
    conn = None
    msg = ""
    try:
        conn = sqlite3.connect(db_file)
        msg += sqlite3.version
    except Error as e:
        msg += e
    return msg, conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def store_user_details():
    global user_system

    qtable = """CREATE TABLE IF NOT EXISTS tasks (
	macid integer PRIMARY KEY,
	useragent text NOT NULL,
    username text,
	language text,
	topic_id integer NOT NULL,
	status_id integer NOT NULL,
	begin_date text NOT NULL,
	end_date text NOT NULL
    );"""

    user_system = request.headers.get('User-Agent')
    msg, conn = create_connection(r"userdata.db")
    msg += gma()
    return msg
