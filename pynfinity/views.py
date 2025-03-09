"""
Routes and views for the flask application.
"""

from datetime import datetime

from flask import render_template, request
from pygments.formatters import HtmlFormatter

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
        print(page_responses)
        # ut.store_user_details()

    return render_template(
        'index.html',
        title='Home Page',
        page_load_params=page_load_params,
        year=datetime.now().year,
        creator=data,
        course_details=ut.content_to_html()
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
