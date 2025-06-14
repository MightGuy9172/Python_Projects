import smtplib
from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL=os.environ['EMAIL']
PASSWORD=os.environ['PASS']
MY_LATITUDE=29.123
MY_LONGITUDE=75.770

#Enter your Mail here
TO="manishmaurya9172@gmail.com"

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data=response.json()["iss_position"]
    latitude=float(data["latitude"])
    longitude=float(data["longitude"])

    if MY_LATITUDE-5<= latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5<= longitude <=MY_LONGITUDE+5:
        return True

def is_night():
    parameters={
        "lat":MY_LATITUDE,
        "lng":MY_LONGITUDE,
        "formatted":0,
    }

    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


#Use this to test
# if True and True:
if is_iss_overhead() and is_night():
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(EMAIL,PASSWORD)
    connection.sendmail(from_addr=EMAIL,to_addrs=TO,msg="Subject:Look up\n\nThe ISS is above in the sky.")