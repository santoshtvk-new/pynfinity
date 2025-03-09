"""
Routes and views for the flask application.
"""
from datetime import datetime
from os.path import join, dirname

import yaml
from flask import render_template, request
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

try:
    import pynfinity.utility as ut
except ModuleNotFoundError:
    import utility as ut
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    """Renders the home page."""

    data = f"Creator!"
    page_load_params = {"wod": "", "msg": ""}

    if request.method == 'GET':
        page_load_params['msg'] = "Welcome " + str(datetime.now())

    if request.method == 'POST':
        page_responses = request.get_json()

    # ut.store_user_details()

    return render_template(
        'index.html',
        title='Home Page',
        page_load_params=page_load_params,
        year=datetime.now().year,
        creator=data,
        code_style=f"{HtmlFormatter().get_style_defs('.highlight')}",
        py_structure_details=all_coding_stuff('python'),
        sql_structure_details=all_coding_stuff('sql'),
        git_structure_details=all_coding_stuff('git')
    )


def all_coding_stuff(language="python"):
    with open(join(dirname(__file__), "static/content/coding_reference.yml")) as f:
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
                                                                PythonLexer(),
                                                                HtmlFormatter())
            python_complete_stuff[toughness] = category
    return python_complete_stuff


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title="☎ Video Call for you",
        year=datetime.now().year,
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Few points about me...'
    )
