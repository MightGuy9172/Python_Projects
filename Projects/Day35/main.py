import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid="Yours"
auth_token="Yours"
# if want to secure the api or auth etc. when uploading code online
# export auth_token=your token
# then use in code os.environ.get("auth_token")
API="3edd9b17ea78a017b027e5e023fa227f"
parameters={
    "lat":29.12,
    "lon":75.77,
    "cnt":4,
    "appid":API,
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
temperature_data=response.json()["list"]

will_rain=False
for data in temperature_data:
    code=data["weather"][0]["id"]
    if code<700:
        will_rain=True

if will_rain:
    proxy_client=TwilioHttpClient()
    proxy_client.session.proxies={'https':os.environ['https_proxy']}
    client=Client(account_sid,auth_token,http_client=proxy_client)
    message=client.messages\
            .create(
            body="It's going to rain Today. Bring Umbrella !",
            from_="Twilio number here",
            to="Verified number here",
    )