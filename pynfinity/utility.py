import datetime
import json
from os.path import join, dirname

import flask
import yaml
from flask import request
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import BashLexer
from pygments.lexers import PythonLexer
from pygments.lexers import SqlLexer
from pygments.lexers import JavaLexer
from pygments.lexers import CLexer
from pygments.lexers import CppLexer

try:
    import sqlite3
    from sqlite3 import Error
    from getmac import get_mac_address as gma
except Exception:
    pass

available_lexer = {
    'python': PythonLexer(),
    'sql': SqlLexer(),
    'linux_shell': BashLexer(),
    'java': JavaLexer(),
    'selenium': JavaLexer(),
    'pandas': PythonLexer(),
    'c': CLexer(),
    'cpp': CppLexer()
}
code_yml_reference = join(dirname(__file__), "static/content/coding_reference.yml")
courses_json_reference = join(dirname(__file__), "static/content/courses.json")
images_directory = join("static", "bg")


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


def all_coding_stuff(language="python"):
    lexer = available_lexer.get(language, PythonLexer())

    with open(code_yml_reference) as f:
        try:
            code_complete = yaml.safe_load(f)
        except Exception as e:
            print(e)
            code_complete = {}

    python_complete_stuff = {}
    yml_py = code_complete[language]
    for toughness in yml_py.keys():
        category = {}
        for k in yml_py[toughness].keys():
            category[yml_py[toughness][k]['title']] = highlight(yml_py[toughness][k]['code'],
                                                                lexer,
                                                                HtmlFormatter())
            python_complete_stuff[toughness] = category
    return python_complete_stuff


def content_to_html():
    courses = json.loads(open(courses_json_reference).read())
    for crs in courses.keys():
        courses[crs]["icon"] = join(images_directory, courses[crs]["icon"])
        courses[crs]["content"] = f"{flask.request.base_url}/courses/{crs}"
        desc = str(courses[crs]["description"]).replace('\n', '<br>')
        for w in ['Key Topics Covered:', 'Basics:', 'Intermediate:', 'Advanced:']:
            if w in desc:
                desc = desc.replace(w, f'<b>{w}</b>')

        courses[crs]["description"] = desc
    print(courses.keys())
    il = list(courses.items())
    return [dict(il[i:i + 3]) for i in range(0, len(il), 3)]
