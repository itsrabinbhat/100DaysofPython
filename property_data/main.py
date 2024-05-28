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

