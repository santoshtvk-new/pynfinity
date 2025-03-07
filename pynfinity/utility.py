import json

from os.path import dirname, join

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

    user_system = request.headers.get("User-Agent")
    msg, conn = create_connection(r"userdata.db")
    msg += gma()
    return msg


def git_menu_list():
    topics = {}
    git_complete = json.load(open(join(dirname(__file__), "static/content/git_reference.json")))
    for i in git_complete:
        if i['chapter'][1] not in topics.keys():
            topics[i['chapter'][1]] = [i['chapter'][0], []]
        
        topics[i['chapter'][1]][1].append({i["id"]:i["Topic"]})
    return topics


def git_content():
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