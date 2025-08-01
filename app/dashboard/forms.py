from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class HealthForm(FlaskForm):
    glucose = FloatField("Glucose Level (mg/dL)", validators=[InputRequired(), NumberRange(min=0)])
    blood_pressure = FloatField("Blood Pressure (mm Hg)", validators=[InputRequired(), NumberRange(min=0)])
    heart_rate = FloatField("Heart Rate (bpm)", validators=[InputRequired(), NumberRange(min=0)])
    weight = FloatField("Weight (kg)", validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField("Submit")
