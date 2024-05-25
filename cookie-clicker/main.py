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
    available_items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
    item_cost_list_obj = driver.find_elements(By.CSS_SELECTOR, value='#store div b')
    item_cost_list = [item.text for item in item_cost_list_obj]
    item_cost_list.pop()
    item_cost_list = [int(item.split(' - ')[1].replace(',', '')) for item in item_cost_list]

    # converting money to int
    try:
        money = int(money.text)
    except ValueError:
        money = money.text.replace(',', '')
        money = int(money)

    # Filtering available_items for only valid items
    available_items = [item for item in available_items if item.get_attribute('onclick') is not None]

    # checking which item can be bought
    # checking from most expensive item since we want to buy expensive one first if possible
    for item_cost in reversed(item_cost_list):
        if item_cost <= int(money):
            print(item_cost, money)
            idx = item_cost_list.index(item_cost)
            buy_item = available_items[idx]
            print(buy_item.get_attribute('id'))
            buy_item.click()
            break


# main loop and setting 5sec delay for purchasing the items
start_time = time.time()
interval = 5

while True:
    cookie.click()
    current_time = time.time()
    if current_time - start_time >= 5:
        purchase_items()
        start_time = current_time
