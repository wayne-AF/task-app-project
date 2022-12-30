from flask import render_template
from taskmanager import app, db
# need to import the classes from models.py in order to generate the database
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")