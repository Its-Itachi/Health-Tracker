from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.auth.forms import RegistrationForm, LoginForm
from app.auth.models import User
from app.extensions import login_manager

# ✅ Define Blueprint at top level — very important
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# 🔐 Registration Route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if username already exists
        if User.get_by_username(form.username.data):
            flash("Username already exists", "danger")
            return redirect(url_for('auth.register'))

        # Create user and log them in
        user = User.create(form.username.data, form.password.data)
        login_user(user)
        flash("Registration successful!", "success")
        return redirect(url_for('dashboard.dashboard'))

    return render_template('auth/register.html', form=form)


# 🔐 Login Route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for('dashboard.dashboard'))
        flash("Invalid username or password", "danger")
    return render_template('auth/login.html', form=form)


# 🔐 Logout Route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('auth.login'))


# 🔄 Load user from session for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
