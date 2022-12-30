import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URL"] = os.environ.get("DB_URL")

# must create instance of SQLAlchemy class
db = SQLAlchemy(app)

# this is imported last because the routes file relies on using both the app
# and db variables defined above.
from taskmanager import routes  # noqa