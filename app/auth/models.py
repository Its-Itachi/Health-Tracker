from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db
from bson.objectid import ObjectId
from datetime import datetime, timedelta

# -------------------------
# 🔐 User Model
# -------------------------
class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.username = user_data['username']
        self.password_hash = user_data['password_hash']

    @staticmethod
    def get(user_id):
        user_data = db.db.users.find_one({'_id': ObjectId(user_id)})
        return User(user_data) if user_data else None

    @staticmethod
    def get_by_username(username):
        user_data = db.db.users.find_one({'username': username})
        return User(user_data) if user_data else None

    @staticmethod
    def create(username, password):
        password_hash = generate_password_hash(password)
        inserted = db.db.users.insert_one({
            'username': username,
            'password_hash': password_hash
        })
        return User.get(inserted.inserted_id)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# -------------------------
# 📋 Health Log Model
# -------------------------
class HealthLog:
    @staticmethod
    def create(user_id, data):
        data['user_id'] = user_id
        data['date'] = datetime.strptime(data['date'], '%Y-%m-%d') if 'date' in data and data['date'] else datetime.utcnow()
        db.db.health_logs.insert_one(data)

    @staticmethod
    def update(entry_id, updated_data):
        if 'date' in updated_data and updated_data['date']:
            updated_data['date'] = datetime.strptime(updated_data['date'], '%Y-%m-%d')
        db.db.health_logs.update_one(
            {'_id': ObjectId(entry_id)},
            {'$set': updated_data}
        )

    @staticmethod
    def delete(entry_id):
        db.db.health_logs.delete_one({'_id': ObjectId(entry_id)})

    @staticmethod
    def get_by_id(entry_id):
        return db.db.health_logs.find_one({'_id': ObjectId(entry_id)})

    @staticmethod
    def get_recent_logs(user_id, limit=10):
        return list(db.db.health_logs.find(
            {'user_id': user_id}
        ).sort('date', -1).limit(limit))

    @staticmethod
    def get_logs_by_user(user_id, days=7):
        cutoff = datetime.utcnow() - timedelta(days=days)
        return list(db.db.health_logs.find({
            'user_id': user_id,
            'date': {'$gte': cutoff}
        }).sort('date'))

    @staticmethod
    def calculate_bmi(weight, height_cm):
        if not weight or not height_cm:
            return None, None
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 1)
        category = HealthLog.get_bmi_category(bmi)
        return bmi, category

    @staticmethod
    def get_bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
