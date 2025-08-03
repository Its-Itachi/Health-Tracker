# 🩺 Health Tracker Dashboard

👉 **Live App**: [https://health-tracker-y82l.onrender.com](https://health-tracker-y82l.onrender.com)

This is a full-stack **health monitoring** web application built with **Flask** and **MongoDB Atlas**, allowing users to log and track daily health metrics such as blood pressure, heart rate, weight, sleep, and more.

---

## 📊 App Features

- 🧾 **Daily Health Log** form with date picker  
- 📈 **Interactive Trend Charts** for 7 / 30 days using Chart.js  
- 🧠 **Smart Insights** based on recent data (e.g. BP rising)  
- 📅 **Edit/Delete entries** by date  
- 💡 **BMI Calculation** with live category classification  
- 🌙 **Sleep Tracking** (hours slept)  
- 🔒 **User Authentication** (Register, Login, Logout)

---

## 🛠 Tech Stack

| Layer      | Tools Used                               |
|------------|------------------------------------------|
| Backend    | Flask (with Blueprints)                  |
| Database   | MongoDB Atlas (Cloud NoSQL)              |
| Auth       | Flask-Login, WTForms                     |
| Frontend   | HTML, CSS, Bootstrap, Chart.js, Jinja2   |
| Deployment | Render                                   |

---

## 🚀 How to Run Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Its-Itachi/Health-Tracker.git
    cd Health-Tracker
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows (PowerShell):
      ```bash
      venv\Scripts\Activate.ps1
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file** in the root directory:
    ```
    SECRET_KEY=mysecretkey123
    MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/health_tracker_db?retryWrites=true&w=majority&appName=health-tracker
    ```

6. **Run the Flask app:**
    ```bash
    python run.py
    ```

7. **Open your browser and visit:**
    ```
    http://localhost:5000
    ```

---

## 🌐 Deployment (Render)

The app is deployed on **Render** and can be accessed live here:  
[https://health-tracker-y82l.onrender.com](https://health-tracker-y82l.onrender.com)

To deploy your own version:

1. Push your project to GitHub
2. Create a Web Service on [https://render.com](https://render.com)
3. Add the following environment variables:
    - `SECRET_KEY` = your secret key
    - `MONGO_URI` = your MongoDB Atlas connection string
4. Set build and start commands:

| Setting         | Value                            |
|----------------|----------------------------------|
| Build Command  | `pip install -r requirements.txt`|
| Start Command  | `python run.py`                  |

---

## 👤 Author

**Name**: Jayesh Dethe  
**GitHub**: [@Its-Itachi](https://github.com/Its-Itachi)

---

## ⭐ Support

If you find this project helpful:

- ⭐ Star the repo on GitHub  
- 🔄 Fork it to customize your own health dashboard  
- 🧠 Share with peers & health communities

---

## 📝 Notes

- MongoDB Atlas must be accessible from your network (whitelist IP or allow 0.0.0.0/0)
- Make sure `.env` variables are set correctly both locally and on Render
- BMI is computed from stored height and current weight
- Chart.js dynamically shows trends for 7 or 30 days
- Only BP, HR, and weight are required; others are optional

---

Stay healthy & keep tracking! 💪📊
