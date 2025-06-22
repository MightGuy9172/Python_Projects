import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


ZILLOW_CLONE_URL="https://appbrewery.github.io/Zillow-Clone/"
FORM_URL="https://docs.google.com/forms/d/e/1FAIpQLSdYByKITDJ7btJ1FO51hFzp-mgUbC4JJDHbHTjZeQJ3UdgRDg/viewform"


#------------------------------BEAUTIFUL SOUP------------------------------
response=requests.get(url=ZILLOW_CLONE_URL)
response.raise_for_status()
soup=BeautifulSoup(response.text,'html.parser')
all_links=soup.select("li article div a")
listing_links=[]
for link in all_links:
    listing_links.append(link.get("href"))

all_prices=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
listing_prices=[]
for price in all_prices:
    listing_prices.append(price.getText().split('+')[0].split('/')[0])

all_addresses=soup.find_all(name="address")
listing_addresses=[]
for address in all_addresses:
    listing_addresses.append(address.getText().strip())


#------------------------------SELENIUM------------------------------
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get(url=FORM_URL)


for i in range(len(listing_prices)):
    address_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd")
    time.sleep(1)
    address_input.send_keys(listing_addresses[i])
    price_input.send_keys(listing_prices[i])
    link_input.send_keys(listing_links[i])
    submit_button.click()
    time.sleep(1)
    another_response = driver.find_element(By.LINK_TEXT, "Submit another response")
    another_response.click()
