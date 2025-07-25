import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

SHEET_ENDPOINT=os.environ['SHEETY']
print(SHEET_ENDPOINT)
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user=os.environ['SHEET_USERNAME']
        print(self._user)
        self._password=os.environ['SHEET_PASSWORD']
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        print(self._password)
        self._author=HTTPBasicAuth(self._user,self._password)
        self.sheet={}
        self.customer_data = {}

    def get_data(self):
        response=requests.get(url=SHEET_ENDPOINT,auth=self._author)
        response.raise_for_status()
        self.sheet=response.json()["prices"]
        return self.sheet

    def put_data(self):
        for row in self.sheet:
            body={
                "price":{
                    "iataCode":row["iataCode"]
                }
            }
            response=requests.put(url=f"{SHEET_ENDPOINT}/{row["id"]}",json=body,auth=self._author)
            response.raise_for_status()

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data