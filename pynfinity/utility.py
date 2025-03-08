import datetime
import json

from os.path import dirname, join
from flask import request

try:
    import sqlite3
    from sqlite3 import Error
    from getmac import get_mac_address as gma
except Exception:
    pass


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def trigger_query_db(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print(c.fetchall())
    except Error as e:
        print(e)


def store_user_details():
    qtable = """CREATE TABLE IF NOT EXISTS UserData(
        macid text PRIMARY KEY,
        useragent text NOT NULL,
        timestamp text NOT NULL
        );"""

    conn = create_connection(r"userdata.db")
    if conn:
        trigger_query_db(conn, qtable)
        insert_table = f"""
            INSERT INTO UserData (macid, useragent, timestamp)
            VALUES ('{gma()}', '{str(request.remote_addr) + ' ' + str(request.user_agent) + ' ' + str(request.remote_user)}', '{str(datetime.datetime.now())}');
            """
        trigger_query_db(conn, insert_table)
        trigger_query_db(conn, "select * from UserData")


def git_menu_list():
    topics = {}
    git_complete = json.load(open(join(dirname(__file__), "static/content/git_reference.json")))
    for i in git_complete:
        if i['chapter'][1] not in topics.keys():
            topics[i['chapter'][1]] = [i['chapter'][0], []]

        topics[i['chapter'][1]][1].append({i["id"]: i["Topic"]})
    return topics


def git_content():
    topic_content = ""
    git_complete = json.load(open(join(dirname(__file__), "static/content/git_reference.json")))
    for i in git_complete:
        count = 1
        li_group = ""
        for o in i["Options"]:
            for k in o:
                li_group += f"<li><span>{k}</span>{o[k]}</li>"

        topic_content += f"""
                        <div class="chapter_content">
                                <h3 id="chapter2-command{str(count)}">{i['Topic']}</h3>
                                <br />
                                <p>{i['Description']}</p>
                                <br />
                                <i>click on code snippet to copy</i>
                                <pre onclick="copyToClipboard('chapter2-command{str(count)}-code')"><code id="chapter2-command{str(count)}-code">{i['Syntax']}</code></pre>
                                <h4 class="code_example">{i['Example']}</h4>
                                <ul class="cmd_params">
                                    {li_group}
                                </ul>
                            </div>
                        """
        count += 1
    return git_complete
