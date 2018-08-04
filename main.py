#!/bin/env python
# main.py

import json
from flask import Flask, render_template, request, Response

import utils.db

app = Flask(__name__)

spam = ['spam', 'ham', 'burger', 'cheese', 'bacon']


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
    return render_template("about.html", ing=spam)


@app.route('/source/<value>', methods=['GET'])
def hello_name(value):
    # return "Hello {}!".format(name)
    data = utils.db.get_color_values(value)
    response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    return response


if __name__ == '__main__':
    app.run(debug=True)
