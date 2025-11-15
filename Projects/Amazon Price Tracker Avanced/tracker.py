import os
import json
import time
import random
import logging
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from db import PriceDB
from emailer import Emailer

load_dotenv()

logging.basicConfig(level=logging.INFO, filename="tracker.log",
                    format='%(asctime)s - %(levelname)s - %(message)s')

MY_EMAIL = os.getenv('EMAIL')
MY_PASSWORD = os.getenv('PASS')

USER_AGENTS = [
    "Mozilla/5.0 Windows NT Chrome",
    "Mozilla/5.0 Windows NT Edge",
    "Mozilla/5.0 Linux Firefox"
]

HEADERS = lambda: {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Language": "en-IN,en;q=0.9"
}

class Tracker:
    def __init__(self):
        self.db = PriceDB()
        self.mailer = Emailer(MY_EMAIL, MY_PASSWORD)

    def load_products(self):
        with open('products.json', 'r') as f:
            return json.load(f)

    def fetch(self, url):
        try:
            r = requests.get(url, headers=HEADERS(), timeout=10)
            r.raise_for_status()
            return r.text
        except:
            return None

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # TITLE
        title_tag = soup.find(id="productTitle")
        title = title_tag.get_text(strip=True) if title_tag else "Unknown Product"

        # PRICE
        try:
            whole_tag = soup.find('span', class_='a-price-whole')
            if not whole_tag:
                price = None
            else:
                whole = whole_tag.get_text(strip=True).replace(',', '')
                price = float(whole)
        except Exception as e:
            price = None

        print(title,price)
        return title, price

    def run(self):
        products = self.load_products()

        for item in products:
            url = item['url']
            threshold = item['threshold']
            to_addr = item.get('email', MY_EMAIL)

            html = self.fetch(url)
            if not html:
                logging.error(f"Failed to fetch: {url}")
                continue

            title, price = self.parse(html)

            pid = self.db.upsert_product(url, title)

            if price is not None:
                self.db.insert_price(pid, price)
                logging.info(f"Checked {title}: ₹{price}")

                if price < threshold:
                    subject = f"Price Drop: {title} now ₹{price}"
                    body = f"""
                    <h3>Price Alert</h3>
                    <p><b>{title}</b></p>
                    <p>Current Price: ₹{price}</p>
                    <p><a href="{url}">Open Amazon</a></p>
                    """
                    self.mailer.send_email(subject, body, to_addr)

            time.sleep(2)

if __name__ == "__main__":
    Tracker().run()