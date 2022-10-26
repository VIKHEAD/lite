from flask import Flask, request, Response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from lite_app.config import DEV_DB, PROD_DB
import os
import secrets
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DEV_DB if os.environ.get("DEBUG") == "1" else PROD_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = secrets.token_hex()
app.config['SECRET_KEY'] = '304da0ded9b209ad36f9182bdfcc8d9a28fbd116694f42ba7f147b78e9e7e48e'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from lite_app import routes
