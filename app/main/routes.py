# app/main/routes.py
from flask import Blueprint, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return redirect(url_for('auth.login'))  # Or 'dashboard.dashboard' if user is already logged in
