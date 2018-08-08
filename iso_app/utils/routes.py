# routes.py

import json
from flask import render_template
from iso_app import app
from iso_app.utils import misc


@app.route("/")
@app.route("/home", methods=['GET'])
def home():
    button_dict= misc.create_button_list()
    return render_template("map.html", button_dict=button_dict)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/source/<value>', methods=['GET'])
def get_source(value):
    """
    For debugging.
    :param value: specific value for get request
    :return: response with status 200 and given data
    """
    data = misc.get_data(value)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
