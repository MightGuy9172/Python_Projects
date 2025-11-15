# Amazon Price Tracker

Amazon Price Tracker is a Python script that monitors the price of a specified Amazon product and sends you an email notification when the price drops below your desired threshold.

## Features

- Scrapes product name and current price from any Amazon product page.
- Sends an email alert when the price falls below your target value.
- Uses environment variables to securely store email credentials and product details.
- Easy configuration via a `.env` file.
- Simple, lightweight, and customizable.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. **Clone this repository:**

   ```sh
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. **Install dependencies:**

   ```sh
   pip install requests beautifulsoup4 python-dotenv
   ```

3. **Configure environment variables:**

   - Copy `.env.example` to `.env`:
     ```sh
     copy .env.example .env
     ```
   - Edit `.env` and set the following variables:
     ```
     PRODUCT_URL=https://www.amazon.in/dp/your_product_id
     TARGET_PRICE=999.99
     EMAIL=your_email@gmail.com
     EMAIL_PASS=your_email_password
     RECIPIENT_EMAIL=recipient_email@gmail.com
     ```

4. **Run the script:**
   ```sh
   python amazon_price_tracker.py
   ```

## Usage

- The script will fetch the product name and price from the URL specified in your `.env` file.
- If the current price is less than or equal to your `TARGET_PRICE`, you will receive an email notification.
- You can schedule this script to run periodically using Task Scheduler (Windows) or cron (Linux/Mac).

## Example `.env` file

```
PRODUCT_URL=https://www.amazon.in/dp/B09XYZ1234
TARGET_PRICE=1500.00
EMAIL=your_email@gmail.com
EMAIL_PASS=your_email_password
RECIPIENT_EMAIL=recipient_email@gmail.com
```

## Notes

- Make sure your email provider allows access from less secure apps or set up an app password if using Gmail.
- Amazon may block requests if too many are made in a short period. Use responsibly.
- For best results, use the script with products available in your region.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
