import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)

# creating a driver
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.daraz.com.np/catalog/?q=shoes+men&_keyori=ss&from=input&spm=a2a0e.searchlist.search.go'
           '.1b863647cmk7xN')

# Extracting title and price of the products
title_list = driver.find_elements(By.ID, value='id-title')
price_list = driver.find_elements(By.ID, value='id-price')

# getting actual values of titles and prices
title_list = [title.text for title in title_list]
price_list = [price.text.split('\n')[0] for price in price_list]

# Creating a text file with scrapped data
with open('data.txt', 'w') as file:
    for i in range(0, len(title_list)):
        text = f"{title_list[i]} --> {price_list[i]}\n"
        file.write(text)
