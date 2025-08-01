from flask_pymongo import PyMongo
from flask_login import LoginManager

db = PyMongo()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # redirect to login page if not authenticated
