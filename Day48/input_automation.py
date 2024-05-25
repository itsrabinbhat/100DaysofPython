from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user_data = {
    'fname': 'John',
    'lname': 'Doe',
    'email': "john@doe.com"
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

# getting elements from the site
fname = driver.find_element(By.NAME, value='fName')
lname = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

# sending data to fill the form
fname.send_keys(user_data['fname'])
lname.send_keys(user_data['lname'])
email.send_keys(user_data['email'], Keys.ENTER)
