from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL=os.environ['EMAIL']
MY_PAASWORD=os.environ['PASS']
# TO_ADDRESS : Enter email to get alert
TO_ADDRESS="mk99962769@gmail.com"
# URL: Product for which u want alert
URL="https://amzn.in/d/fhxDxLG"


header={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Accept-Language":"en-US,en;q=0.9,en-IN;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
}


response=requests.get(url=URL,headers=header)
response.raise_for_status()
data=BeautifulSoup(response.text,'html.parser')
product_name=data.find(name="span",id="productTitle").getText().strip()
product_price=float(data.find(name="span",class_="a-price-whole").getText())


#FOR TESTING
if( product_price < 800 ):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PAASWORD)
        content=f"Awesome Deal 🔥🔥\n\n{product_name} is now ₹{product_price} : {URL}"
        msg = MIMEText(content, _charset="utf-8")
        msg['Subject'] = "Amazon Price Tracker"
        msg['From'] = MY_EMAIL
        msg['To'] = TO_ADDRESS
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS, msg=msg.as_string())