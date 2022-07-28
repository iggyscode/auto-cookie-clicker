from os import environ
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


load_dotenv()

# -- Auto cookie clicker --- 
# -- SELENIUM 4.3 -- -------
chromium_path = str(environ.get("CHROME_DRIVER_PATH"))
driver = webdriver.Chrome(executable_path=chromium_path) 

driver.get("https://orteil.dashnet.org/experiments/cookie/")

ID ='id'
CSS_SELECTOR = 'css selector'

#How long to run the bot
program_timer = time.time() + 60 * 1

#Needed elements on the page
cookie = driver.find_element(By.ID, 'cookie')
element_names = ['buyCursor', 'buyGrandma', "buyFactory", 'buyMine', 'buyShipment', 'buyAlchemy lab', 'buyTime machine']


def is_purchasable(item_name):
    unpurchasable_items = [item.get_attribute('id') for item in driver.find_elements(By.CSS_SELECTOR, ".grayed")]

    if (item_name in unpurchasable_items) :
        return False
    else:
        return True


# Bot runtime
while time.time() < program_timer:

    cookie_timer = time.time() + 5
    while time.time() < cookie_timer:
        cookie.click()
    
    prices = []

    for element in element_names:
        if is_purchasable(element):
            prices.append(int(
            driver.find_element(By.ID, element)
            .text
            .split('\n')[0]
            .split('-')[-1]
            .strip()
            .replace(',', '')
            ))

    most_expensive_item = driver.find_element(By.ID, element_names[prices.index(prices[-1])])
    most_expensive_item.click()

driver.quit()