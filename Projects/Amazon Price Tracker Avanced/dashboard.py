from flask import Flask, send_file, request, render_template_string
import sqlite3
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import datetime


DB_FILE = "prices.db"
app = Flask(__name__)

TEMPLATE = """
<h2>Tracked Products</h2>
<ul>
{% for p in products %}
  <li><a href="/plot?id={{p[0]}}">{{p[1]}}</a></li>
{% endfor %}
</ul>
"""

@app.route('/')
def index():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT id, title FROM products")
        products = c.fetchall()
    return render_template_string(TEMPLATE, products=products)

@app.route('/plot')
def plot():
    pid = request.args.get('id')
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('SELECT price, checked_at FROM prices WHERE product_id=?', (pid,))
        rows = c.fetchall()

    prices = [r[0] for r in rows]
    dates = [datetime.fromisoformat(r[1]) for r in rows]

    fig, ax = plt.subplots()
    ax.plot(dates, prices, marker='o')
    ax.set_title('Price History')
    ax.set_xlabel('Date')
    ax.set_ylabel('₹ Price')
    fig.autofmt_xdate()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
