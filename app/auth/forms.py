from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, FloatField, DateField
)
from wtforms.validators import InputRequired, Length, EqualTo, Optional, DataRequired

# 🔐 Registration Form
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=4, max=25)],
        render_kw={"placeholder": "e.g. itachi123"}
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6)],
        render_kw={"placeholder": "Enter password"}
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[InputRequired(), EqualTo('password', message='Passwords must match')],
        render_kw={"placeholder": "Re-enter password"}
    )
    submit = SubmitField("Register")

# 🔐 Login Form
class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired()],
        render_kw={"placeholder": "Your username"}
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired()],
        render_kw={"placeholder": "Your password"}
    )
    submit = SubmitField("Login")

# 📋 Daily Health Data Form
class HealthDataForm(FlaskForm):
    glucose = FloatField(
        'Glucose (mg/dL)',
        validators=[Optional()],
        render_kw={"placeholder": "e.g. 110"}
    )
    blood_pressure = FloatField(
        'Blood Pressure (mm Hg)',
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g. 120"}
    )
    heart_rate = FloatField(
        'Heart Rate (bpm)',
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g. 75"}
    )
    weight = FloatField(
        'Weight (kg)',
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g. 68"}
    )
    height = FloatField(
        'Height (cm)',
        validators=[Optional()],
        render_kw={"placeholder": "e.g. 170"}
    )
    sleep_hours = FloatField(
        'Sleep (hrs)',
        validators=[Optional()],
        render_kw={"placeholder": "e.g. 7.5"}
    )
    date = DateField(
        'Date (optional)',
        format='%Y-%m-%d',
        validators=[Optional()],
        render_kw={"placeholder": "YYYY-MM-DD"}
    )
    submit = SubmitField('Save')
