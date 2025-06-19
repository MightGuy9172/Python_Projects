from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60*5

cookie = driver.find_element(by=By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()
    #check ever 5sec
    if time.time()>timeout:
        all_items=driver.find_elements(By.CSS_SELECTOR, "#store b")
        items_prices=[]

        #taking prices of items in a list
        for item in all_items:
            element_text = item.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                items_prices.append(cost)

        #taking price value as key and value as id of that item
        cookie_upgrades = {}
        for n in range(len(items_prices)-1):
            cookie_upgrades[items_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #check cookie count by comparing to cookie items dictionary and store that in new dictionary which can be purchased
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        #select max from the affordable items
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        #click that item to upgrade
        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break


driver.quit()
