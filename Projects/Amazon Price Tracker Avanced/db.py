import sqlite3
from datetime import datetime, timezone

DB_FILE = "prices.db"

class PriceDB:
    def __init__(self, db_path=DB_FILE):
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                url TEXT UNIQUE,
                title TEXT
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS prices (
                id INTEGER PRIMARY KEY,
                product_id INTEGER,
                price REAL,
                checked_at TEXT,
                FOREIGN KEY(product_id) REFERENCES products(id)
            )''')
            conn.commit()

    def upsert_product(self, url, title):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()

            c.execute('INSERT OR IGNORE INTO products (url, title) VALUES (?, ?)', (url, title))
            conn.commit()

            c.execute('SELECT id FROM products WHERE url = ?', (url,))
            return c.fetchone()[0]

    def insert_price(self, product_id, price):
        now = datetime.now(timezone.utc).isoformat()
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO prices (product_id, price, checked_at) VALUES (?, ?, ?)',
                      (product_id, price, now))
            conn.commit()

    def get_prices(self, product_id):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('SELECT price, checked_at FROM prices WHERE product_id=? ORDER BY id ASC', (product_id,))
            return c.fetchall()