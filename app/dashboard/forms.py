from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, DateField
from wtforms.validators import InputRequired, Optional, NumberRange
from datetime import date

class HealthForm(FlaskForm):
    glucose = FloatField(
        "Glucose (mg/dL)",
        validators=[Optional(), NumberRange(min=0)],
        render_kw={"placeholder": "e.g. 110"}
    )

    blood_pressure = FloatField(
        "Blood Pressure (mm Hg)",
        validators=[InputRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "e.g. 120"}
    )

    heart_rate = FloatField(
        "Heart Rate (bpm)",
        validators=[InputRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "e.g. 75"}
    )

    weight = FloatField(
        "Weight (kg)",
        validators=[InputRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "e.g. 70"}
    )

    height = FloatField(
        "Height (cm)",
        validators=[Optional(), NumberRange(min=0)],
        render_kw={"placeholder": "e.g. 170"}
    )

    sleep_hours = FloatField(
        "Sleep Duration (hrs)",
        validators=[Optional(), NumberRange(min=0, max=24)],
        render_kw={"placeholder": "e.g. 7.5"}
    )

    date = DateField(
        "Date",
        default=date.today,
        format='%Y-%m-%d',
        validators=[Optional()],
        render_kw={"placeholder": "YYYY-MM-DD"}
    )

    submit = SubmitField("Save Entry")
