# routes.py

import json
from flask import render_template, url_for, flash, redirect
from iso_app import app
from iso_app.utils.iso import ISO
from iso_app.utils import db


@app.route("/")
@app.route("/home", methods=['GET'])
def home():
    return render_template("map.html")


@app.route("/get", methods=['GET'])
def get():
    # if request.method == "GET":
    #     url = request.form['url']
    # return {'DK': 'id', 'desc': 'test'}
    data = {'DK': 'id', 'desc': 'test'}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/about")
def about():
    spam = ['spam', 'ham', 'burger', 'cheese', 'bacon']
    return render_template("about.html", ing=spam)


@app.route('/source/<value>', methods=['GET'])
def get_source(value):
    # return "Hello {}!".format(name)
    print(value)
    data = db.get_color_values(int(value))
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/desc', methods=['GET'])
def get_desc():
    # data = db.get_description()
    data = {}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


iso = ISO.query.filter_by(iso2='DE').first()
print(iso)
