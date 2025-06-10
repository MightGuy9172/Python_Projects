import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid="Yours"
auth_token="Yours"
# if want to secure the api or auth etc. when uploading code online
# export auth_token=your token
# then use in code os.environ.get("auth_token")
STOCK = "RELIANCE.BSE"
COMPANY_NAME = "Reliance Industries"
STOCK_API_KEY="YOURS"
STOCK_ENDPOINT="https://www.alphavantage.co/query"

NEWS_ENDPOINT="https://newsapi.org/v2/everything"
NEWS_API_KEY="YOURS"

parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":STOCK_API_KEY,
}

#-------------STOCK---------------
response=requests.get(url=STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]

yesterday_data=data_list[0]
yesterday_close_price=yesterday_data["4. close"]

dayBefore_yesterday_data=data_list[1]
dayBefore_yesterday_close_price=dayBefore_yesterday_data["4. close"]

difference=float(yesterday_close_price)-float(dayBefore_yesterday_close_price)
diff_percent=round(difference/float(yesterday_close_price))*100

up_down=None
if difference>0:
    up_down="🔺"
else:
    up_down="🔻"

#--------------NEWS-------------
if abs(diff_percent) > 0:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()["articles"]
    articles = news_data[:3]

    formatted_article = [f'{STOCK}:{up_down} {diff_percent}%\nHeadline:{page["title"]}. \nBrief: {page["description"]}' for page in articles]

#---------TWILIO-----------------
    for page in formatted_article:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages \
            .create(
            body=page,
            from_="Twilio number here",
            to="Verified number here",
        )