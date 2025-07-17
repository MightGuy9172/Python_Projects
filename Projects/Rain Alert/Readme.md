# 🌧️ Rain Alert Notification App

A Python script that checks the weather forecast and sends an SMS alert if it's likely to rain. Stay dry and informed with this automated weather notifier!

---

## 🔍 What It Does

- Connects to a **Weather API** to check the forecast.
- Parses the hourly forecast data.
- Sends an **SMS alert** (via Twilio or similar service) if rain is expected.
- Can be scheduled to run automatically using Task Scheduler (Windows) or cron (Linux/Mac).

---

## 🛠️ Built With

- 🐍 **Python 3**
- ☁️ **Requests** – for calling the weather API
- 📦 **Twilio (or any SMS API)** – for sending SMS alerts
- 🔐 Environment variables for API keys (recommended)

---

## 🚀 How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/MightGuy9172/Python_Projects.git
```

3. Run the main application file:

```sh
python main.py
```
