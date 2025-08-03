from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.dashboard.forms import HealthForm
from app.auth.models import HealthLog
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard_bp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = HealthForm()
    editing_id = request.args.get('edit')
    editing_entry = HealthLog.get_by_id(editing_id) if editing_id else None

    if editing_entry:
        if request.method == 'GET':
            form.glucose.data = editing_entry.get('glucose')
            form.blood_pressure.data = editing_entry.get('blood_pressure')
            form.heart_rate.data = editing_entry.get('heart_rate')
            form.weight.data = editing_entry.get('weight')
            form.height.data = editing_entry.get('height')
            form.sleep_hours.data = editing_entry.get('sleep_hours')
            if 'date' in editing_entry:
                d = editing_entry['date']
                if isinstance(d, str):
                    form.date.data = datetime.strptime(d, "%Y-%m-%d").date()
                else:
                    form.date.data = d.date()

    if form.validate_on_submit():
        entry_data = {
            'glucose': form.glucose.data,
            'blood_pressure': form.blood_pressure.data,
            'heart_rate': form.heart_rate.data,
            'weight': form.weight.data,
            'height': form.height.data,
            'sleep_hours': form.sleep_hours.data,
            'date': form.date.data.strftime('%Y-%m-%d') if form.date.data else datetime.utcnow().strftime('%Y-%m-%d')
        }

        if editing_entry:
            HealthLog.update(editing_id, entry_data)
            flash("Health entry updated!", "success")
        else:
            HealthLog.create(current_user.id, entry_data)
            flash("Health data saved!", "success")

        return redirect(url_for('dashboard.dashboard'))

    # 🔁 Trend range toggle (7/30)
    days = int(request.args.get('days', 7))
    logs = HealthLog.get_logs_by_user(current_user.id, days=days)
    recent_logs = HealthLog.get_recent_logs(current_user.id)

    # 📈 Labels + values
    labels = []
    for log in logs:
        d = log.get('date')
        if isinstance(d, str):
            try:
                d = datetime.strptime(d, "%Y-%m-%d")
            except ValueError:
                continue
        labels.append(d.strftime('%Y-%m-%d'))

    glucose = [log.get('glucose') for log in logs]
    bp = [log.get('blood_pressure') for log in logs]
    heart = [log.get('heart_rate') for log in logs]
    weight = [log.get('weight') for log in logs]
    sleep = [log.get('sleep_hours') for log in logs]  # ✅ New: sleep data

    # 🧮 BMI logic
    bmi, category = None, None
    if recent_logs:
        latest = recent_logs[0]
        bmi, category = HealthLog.calculate_bmi(latest.get('weight'), latest.get('height'))

    # 🧠 Smart Insight
    insight = None
    if is_bp_rising(logs):
        insight = "Your blood pressure has been rising. Consider monitoring it more closely."

    return render_template('dashboard/dashboard.html',
                           form=form,
                           editing_entry=editing_entry,
                           records=recent_logs,
                           labels=labels,
                           glucose=glucose,
                           bp=bp,
                           heart=heart,
                           weight=weight,
                           sleep=sleep,  # ✅ sent to template
                           trend_days=days,
                           bmi=bmi,
                           bmi_category=category,
                           insights=insight)


@dashboard_bp.route('/delete/<entry_id>')
@login_required
def delete_entry(entry_id):
    HealthLog.delete(entry_id)
    flash("Entry deleted successfully.", "info")
    return redirect(url_for('dashboard.dashboard'))


@dashboard_bp.route('/edit/<entry_id>')
@login_required
def edit_entry(entry_id):
    return redirect(url_for('dashboard.dashboard', edit=entry_id))


def is_bp_rising(logs):
    """Detect rising BP pattern"""
    bp_values = [log.get('blood_pressure') for log in logs if log.get('blood_pressure') is not None]
    if len(bp_values) < 3:
        return False
    return all(bp_values[i] < bp_values[i + 1] for i in range(len(bp_values) - 2))
