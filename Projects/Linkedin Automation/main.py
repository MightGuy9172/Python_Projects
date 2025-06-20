from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_EMAIL = os.getenv("ACCOUNT")
LINKEDIN_PASSWORD = os.getenv("PASS")

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get(url="https://www.linkedin.com/jobs/search/?"
               "currentJobId=4252712452&f_LF=f_AL&"
               "geoId=102713980&"
               "keywords=python%20developer&"
               "origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true")



# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()


time.sleep(1.5)
email_text=driver.find_element(By.ID,"base-sign-in-modal_session_key")
email_text.send_keys(LINKEDIN_EMAIL)

pass_in=driver.find_element(By.ID,"base-sign-in-modal_session_password")
pass_in.send_keys(LINKEDIN_PASSWORD)
pass_in.send_keys(Keys.ENTER)

input("Captcha Done: ")

time.sleep(3)
easy_apply=driver.find_element(By.ID,"jobs-apply-button-id")
easy_apply.click()

time.sleep(1)
phone=driver.find_element(By.CLASS_NAME,"artdeco-text-input--input")
phone.send_keys("1234567890")

# Locate modal container (scrollable part)
modal = driver.find_element(By.CLASS_NAME, "artdeco-modal__content")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal)

time.sleep(2)
next_btn=driver.find_element(By.CSS_SELECTOR,".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
next_btn.click()

time.sleep(1)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal)
time.sleep(1)
next_btn.click()


time.sleep(1)
exp=driver.find_elements(By.TAG_NAME,"input")
for i in range(3):
    exp[i].send_keys("0")

driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal)
time.sleep(1)
rev_btn=driver.find_element(By.CSS_SELECTOR,".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
rev_btn.click()
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal)

