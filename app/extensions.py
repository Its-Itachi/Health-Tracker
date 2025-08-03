from flask_pymongo import PyMongo
from flask_login import LoginManager

# 🔌 Initialize MongoDB connection
db = PyMongo()

# 🔐 Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirect to login page if user is not logged in
