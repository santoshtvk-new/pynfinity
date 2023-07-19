"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
try:
    import requests
    import sqlite3
    from sqlite3 import Error
    from getmac import get_mac_address as gma
except Exception:
    pass


from flask import Flask
app = Flask(__name__)

import pynfinity.views

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


@app.route('/', methods =["GET", "POST"])
@app.route('/home', methods =["GET", "POST"])
def home():
    """Renders the home page."""

    data = "Creator!" # store_user_details()
    
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        creator=data
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Meet me @ ...',
        year=datetime.now().year,
        message='Let\'s have a cup of Coffee together!'
    )

@app.route('/problems')
def problems():
    """Renders the problems page."""
    return render_template(
        'problems.html',
        title='Coding Challenges',
        year=datetime.now().year,
        message='Let\'s Brain-Storm !!'
    )

@app.route('/experiment')
def experiment():
    """Renders the experiment page."""
    return render_template(
        'experiment.html',
        title='Embedded and Python Projects',
        year=datetime.now().year,
        message='Let\'s Brain-Storm !!'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

