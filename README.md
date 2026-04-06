# weather-app

# 🌦️ Django Weather App

A simple weather application built using **Django** that allows users to search for any city and get real-time weather information.

---

## 🚀 Features

* 🔍 Search weather by city name
* 🌡️ Displays temperature in Celsius
* ☁️ Weather description (clear, cloudy, etc.)
* 📍 Latitude and Longitude
* 🌤️ Weather icon display
* ⚡ Fast and simple UI

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **API:** OpenWeatherMap API

---

## 📂 Project Structure

```
weather-app/
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│
├── myapp/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── templates/
│   │   └── index.html
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

---

### 2️⃣ Create virtual environment

```
python -m venv env
env\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the server

```
python manage.py runserver
```

---

### 5️⃣ Open in browser

```
http://127.0.0.1:8000/
```

---

## 🔑 API Setup

* Get your API key from: https://openweathermap.org/api
* Add your API key in `views.py`

Example:

```
api_key = "YOUR_API_KEY"
```

---

## 📸 Screenshots

*Add your project screenshots here*

---

## 🤝 Contributing

Feel free to fork this repository and contribute!

---

## 📄 License

This project is open-source and free to use.

---

## 🙌 Author

**Your Name**
GitHub: https://github.com/yourusername

---
