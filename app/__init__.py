from flask import Flask
from app.extensions import db, login_manager
from app.auth.routes import auth_bp
from app.dashboard.routes import dashboard_bp
from app.main.routes import main_bp  # ✅ Optional landing page blueprint
from dotenv import load_dotenv
import os

def create_app():
    # 🔐 Load environment variables from .env file
    load_dotenv()

    # 🚀 Create Flask app instance
    app = Flask(__name__)

    # ⚙️ App Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'super-secret-key')
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')  # Will use Atlas if defined in .env

    # 🔌 Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # 🔒 Login manager settings
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # 🔗 Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(main_bp)  # Optional: Landing page

    return app
