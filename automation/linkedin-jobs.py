import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = 'test@test.com'
passwd = 'testpassword'

# creating a chrome driver
chrome_options = webdriver.EdgeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=chrome_options)

# Accessing LinkedIn
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
driver.get(url)

# logging into LinkedIn
email_field = driver.find_element(By.XPATH, value='//*[@id="username"]')
passwd_field = driver.find_element(By.XPATH, value='//*[@id="password"]')
email_field.send_keys(username)
time.sleep(3)
passwd_field.send_keys(passwd, Keys.ENTER)


