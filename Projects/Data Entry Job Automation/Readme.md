# Data Entry Job Automation

This project automates the process of extracting real estate listings from a Zillow clone website and submitting the data to a Google Form.

## Features

- Scrapes property addresses, prices, and links using BeautifulSoup.
- Automatically fills and submits a Google Form for each listing using Selenium.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [selenium](https://pypi.org/project/selenium/)
- Chrome browser and [ChromeDriver](https://chromedriver.chromium.org/downloads)

## Usage

1. Install dependencies:
   ```sh
   pip install requests beautifulsoup4 selenium
   ```
2. Download and place ChromeDriver in your PATH.
3. Run the script:
   ```sh
   python main.py
   ```

## Files

- [`main.py`](main.py): Main automation script.
- [`Readme.md`](Readme.md): Project documentation.
