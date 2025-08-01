from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.dashboard.forms import HealthForm
from app.extensions import db
from datetime import datetime
from bson import ObjectId  # Needed for deleting by _id

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = HealthForm()

    # Handle form submission
    if form.validate_on_submit():
        db.db.health_data.insert_one({
            'user_id': current_user.id,
            'glucose': form.glucose.data,
            'blood_pressure': form.blood_pressure.data,
            'heart_rate': form.heart_rate.data,
            'weight': form.weight.data,
            'timestamp': datetime.utcnow()
        })
        flash("Health data saved!", "success")
        return redirect(url_for('dashboard.dashboard'))

    # Fetch latest 10 records (newest first, then reversed to oldest-first view)
    records = list(db.db.health_data.find({'user_id': current_user.id}).sort('timestamp', -1).limit(10))
    records.reverse()

    # Prepare Chart.js data arrays
    timestamps = [r['timestamp'].strftime("%Y-%m-%d") for r in records]
    glucose = [r['glucose'] for r in records]
    bp = [r['blood_pressure'] for r in records]
    heart = [r['heart_rate'] for r in records]
    weight = [r['weight'] for r in records]

    return render_template('dashboard/dashboard.html',
                           form=form,
                           records=records,
                           labels=timestamps,
                           glucose=glucose,
                           bp=bp,
                           heart=heart,
                           weight=weight)

@dashboard_bp.route('/delete/<entry_id>', methods=['GET'])
@login_required
def delete_entry(entry_id):
    try:
        db.db.health_data.delete_one({
            '_id': ObjectId(entry_id),
            'user_id': current_user.id
        })
        flash("Entry deleted successfully.", "info")
    except Exception as e:
        flash("Error deleting entry.", "danger")
    return redirect(url_for('dashboard.dashboard'))
