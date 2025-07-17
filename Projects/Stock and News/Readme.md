# 📈 Stock Price Alert & News Notification System

A Python project that sends you real-time alerts when a stock price changes significantly, along with the **top news headlines** related to that stock.  
It combines stock market data and news APIs to keep you instantly informed.

---

## 🔍 What It Does

- Checks the **percentage change** in stock price (e.g., TSLA)
- If the change exceeds a threshold (e.g., 5%), it fetches:
  - Top 3 news articles about the company
  - Sends a **detailed SMS alert** via Twilio with headline + summary

---

## 🛠️ Built With

- 🐍 **Python 3**
- 🔄 [Alpha Vantage API](https://www.alphavantage.co/) – for stock price data
- 📰 [NewsAPI](https://newsapi.org/) – for recent news headlines
- 📩 [Twilio API](https://www.twilio.com/) – for sending SMS notifications
- 🔐 `dotenv` – to securely manage API keys

---

## 🚀 How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/MightGuy9172/Python_Projects.git
```

#### Run the main application file:

```sh
python main.py
```
