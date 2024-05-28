# importing necessary libs
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# getting data from property website
res = requests.get('https://appbrewery.github.io/Zillow-Clone/')

# extracting userful data using bs4
sp = BeautifulSoup(res.text, 'html.parser')
property_addr_list = sp.find_all('address', attrs={'data-test': 'property-card-addr'})
property_price_list = sp.find_all('span', attrs={'data-test': 'property-card-price'})
property_url_list = sp.find_all('a', attrs={'data-test': 'property-card-link'})

# Cleaning up the extracted data
property_addr_list = [addr.text.strip() for addr in property_addr_list]
property_price_list = [price.text.replace('+/mo', '').replace('+ 1 bd', '').replace('/mo', '').replace('+ 1bd', '') for
                       price in property_price_list]
property_url_list = [url.get('href') for url in property_url_list]
# print(property_addr_list[0].replace(', 747 Geary St', ''))


# creating a chrome driver with selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# filling google form
for i in range(len(property_addr_list)):
    driver.get('https://forms.gle/TSYipRGDqEBC46bMA')

    # getting form fields from google forms
    addr_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                     '2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                      '2]/div/div[1]/div/div[1]/input')
    url_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                    '2]/div/div[1]/div[2]/textarea')

    submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # populating the form fields
    addr_field.send_keys(property_addr_list[i])
    price_field.send_keys(property_price_list[i])
    url_field.send_keys(property_url_list[i])
    submit_btn.click()
    print(f'Sending data set {i}')
    time.sleep(1)

print('Program completed!')