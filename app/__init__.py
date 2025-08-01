from flask import Flask
from app.extensions import db, login_manager
from app.auth.routes import auth_bp
from app.dashboard.routes import dashboard_bp
from app.main.routes import main_bp   # ✅ NEW
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables from .env
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'super-secret-key')
    app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/health_tracker_db')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(main_bp)  # ✅ NEW

    return app
