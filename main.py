#!/bin/env python
# main.py

from flask import Flask, render_template

app = Flask(__name__)

spam = ['spam', 'ham', 'burger', 'cheese', 'bacon']


@app.route("/")
@app.route("/home")
def home():
    return render_template("map.html")


@app.route("/about")
def about():
    return render_template("about.html", ing=spam)


if __name__ == '__main__':
    app.run(debug=True)
