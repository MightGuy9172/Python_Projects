# Amazon Price Tracker

The **Amazon Price Tracker** is a Python-based application designed to monitor the price of Amazon products and notify users via email when the price drops below a specified threshold. This tool helps users save money by keeping track of product price fluctuations automatically.

---

## **Features**

* Scrapes the product name and current price from Amazon product pages.
* Sends automated email notifications when prices drop below a user-defined threshold.
* Securely stores email credentials and product information using environment variables.
* Allows multiple products to be tracked through a JSON configuration file.
* Includes a visual **price history dashboard** using **Matplotlib** and **Flask**.
* Lightweight, customizable, and easy to set up.

---

## **Requirements**

* **Python 3.x**
* **Libraries:**

  * [requests](https://pypi.org/project/requests/)
  * [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
  * [python-dotenv](https://pypi.org/project/python-dotenv/)
  * **Flask**
  * **Matplotlib**
  * **Pillow**

---

## **Setup Instructions**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   * Copy `.env.example` to `.env`:

     ```bash
     copy .env.example .env
     ```
   * Edit `.env` and provide your credentials:

     ```
     EMAIL=your_email@gmail.com
     PASS=your_email_password
     ```

4. **Configure products:**

   * Open `products.json` and add products with their URLs, price thresholds, and recipient emails:

     ```json
     [
       {
         "url": "https://amzn.in/d/fhxDxLG",
         "threshold": 800,
         "email": "recipient_email@gmail.com"
       }
     ]
     ```

5. **Run the tracker:**

   ```bash
   python tracker.py
   ```

6. **View price history dashboard (optional):**

   ```bash
   python dashboard.py
   ```

   * Open `http://127.0.0.1:5000/` in a browser to see tracked products and price trends.

---

## **How It Works**

1. The script fetches product pages from Amazon using **Requests** and parses HTML with **BeautifulSoup**.
2. Product price and title are extracted and stored in an **SQLite** database.
3. The script compares the current price with the defined threshold.
4. If the price is below the threshold, an automated email is sent using **SMTP**.
5. All product prices are logged, and the **Flask** dashboard can visualize price history with **Matplotlib**.

---

## **Usage Notes**

* Ensure your email provider allows SMTP access or use an **app-specific password** for Gmail.
* Avoid sending too many requests in a short time to prevent being blocked by Amazon.
* The tracker works best with Amazon product URLs from your specific region.

---

## **Security Tips**

* Do **not hardcode passwords** in your scripts. Always use `.env` for sensitive credentials.
* Keep your `.env` file secure and add it to `.gitignore`.

---

## **License**

This project is licensed under the MIT License.
