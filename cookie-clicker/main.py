import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By

# creating a chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# Scrapping data from web
driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, value='cookie')


# Some functions
def purchase_items():
    money = driver.find_element(By.ID, value='money')
    available_items = driver.find_elements(By.CSS_SELECTOR, value='#store div b')
    available_items = [item.text for item in available_items]
    available_items.pop()
    print(available_items)
    print(money.text)


# main loop and setting 5sec delay for purchasing the items
start_time = time.time()
interval = 5

while True:
    cookie.click()
    current_time = time.time()
    if current_time - start_time >= 5:
        purchase_items()
        start_time = current_time

