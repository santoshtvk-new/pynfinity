"""
Routes and views for the flask application.
"""
from datetime import datetime
from os.path import join

import flask
from flask import render_template, request, jsonify
from pygments.formatters import HtmlFormatter

try:
    import pynfinity.utility as ut
    import pynfinity.testing_api as tapi
except ModuleNotFoundError:
    import utility as ut
    import testing_api as tapi
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
        print(page_responses)
        # ut.store_user_details()

    return render_template(
        'index.html',
        title='Home Page',
        page_load_params=page_load_params,
        year=datetime.now().year,
        creator=data,
        course_details=ut.content_to_html(),
        app_navigate='https://pynfinity.com/welcome/testapi'
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title="☎ Wish to Connect",
        year=datetime.now().year,
    )


@app.route('/courses/<course_name>')
@app.route('/home/courses/<course_name>')
def course_content(course_name):
    """Renders the contact page."""
    return render_template(
        'courses.html',
        title=str(course_name).upper(),
        year=datetime.now().year,
        course=course_name,
        code_style=f"{HtmlFormatter().get_style_defs('.highlight')}",
        code_structure_details=ut.all_coding_stuff(course_name)
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


@app.route('/testapi')
def testapi():
    """Renders the api_test_ui page."""
    return render_template(
        'api_playground.html',
        title='API Playground',
        year=datetime.now().year
    )


@app.route('/testapi/<datatype>', methods=["GET", "POST", 'PATCH', 'PUT', 'DELETE'])
@app.route('/testapi/<datatype>/<sc_expected>', methods=["GET", "POST", 'PATCH', 'PUT', 'DELETE'])
def api_testing(datatype="", sc_expected=200):
    if datatype == "help":
        return jsonify({
            "INFO": "This endpoint extension is for Learning & Playing on FLASK-REST-APIs",
            "WARN": "Data beyond below combinations and rules are Ignored",
            "SUGGESTIONS|IMPROVEMENTS|RISK": "https://pynfinity.com/welcome/contact",
            "METHODS ACCEPTED": ["GET", "POST", 'PATCH', 'PUT', 'DELETE'],
            "USAGE": {
                "GET METHOD": {
                    "ENDPOINT": "https://pynfinity.com/welcome/testapi/<datatype>/<status_code_expected>",
                    "DATATYPES": "JSON/XML/TEXT",
                    "STATUS_CODE_EXPECTED": "Any Integer Number [To play around different status_codes and its Names]",
                    "Examples": [
                        "https://pynfinity.com/welcome/testapi/json"
                        "https://pynfinity.com/welcome/testapi/text/204"
                        "https://pynfinity.com/welcome/testapi/xml/400"
                    ]
                },
                "GET METHOD WITH QUERY PARAM": {
                    "ENDPOINT": "https://pynfinity.com/welcome/testapi/QP?key=value",
                    "Examples": [
                        "https://pynfinity.com/welcome/testapi/QP?user=santosh",
                        "https://pynfinity.com/welcome/testapi/qp?user=&age=",
                        "https://pynfinity.com/welcome/testapi/qp?user=santosh&age=30"
                    ]
                },
                "POST METHOD": {
                    "ENDPOINT": "https://pynfinity.com/welcome/testapi/post",
                    "PAYLOAD": "JSON | [Mandatory: at-least empty brackets are required Ex: {}",
                    "---UPCOMING---": "---MULTI_FORM DATA | FILES | DIFFERENT FORMATS---"
                },
                "PUT METHOD": {
                    "ENDPOINT": "https://pynfinity.com/welcome/testapi/<icon-names as unique identifier>/<status_code_expected>",
                    "Example": [
                        "https://pynfinity.com/welcome/testapi/cpp.svg",
                        "https://pynfinity.com/welcome/testapi/pandas",
                        "https://pynfinity.com/welcome/testapi/pandas/202",
                    ],
                    "PAYLOAD": "JSON data for unique_identifier mentioned",
                    "ICON_NAMES|UNIQUE-IDENTIFIER": "Refer GET JSON METHOD"
                },
                "PATCH METHOD": {
                    "ENDPOINT": "https://pynfinity.com/welcome/testapi/<icon-names as unique identifier>/<status_code_expected>",
                    "Example": [
                        "https://pynfinity.com/welcome/testapi/cpp.svg",
                        "https://pynfinity.com/welcome/testapi/pandas",
                        "https://pynfinity.com/welcome/testapi/pandas/202",
                    ],
                    "PAYLOAD": "JSON data for any/all keys in unique_identifier mentioned",
                    "ICON_NAMES|UNIQUE-IDENTIFIER": "Refer GET JSON METHOD"
                },
                "DELETE METHOD": {
                    "ENDPOINT": "https://pynfinity.com/welcome/testapi/<icon-names as unique identifier>/<status_code_expected>",
                    "Example": [
                        "https://pynfinity.com/welcome/testapi/cpp.svg",
                        "https://pynfinity.com/welcome/testapi/pandas",
                        "https://pynfinity.com/welcome/testapi/pandas/202",
                    ],
                    "ICON_NAMES|UNIQUE-IDENTIFIER": "Refer GET JSON METHOD"
                }
            }
        })
    try:
        sc_expected = int(sc_expected)
    except Exception:
        sc_expected = 200
    return tapi.different_responses_api(request, datatype, sc_expected)
