import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = 'itsrabio7@gmail.com'
passwd = '@L1nk3d1no7'

# creating a chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# Accessing LinkedIn
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
driver.get(url)

# logging into LinkedIn
email_field = driver.find_element(By.XPATH, value='//*[@id="username"]')
passwd_field = driver.find_element(By.XPATH, value='//*[@id="password"]')
email_field.send_keys(username)
time.sleep(1)
passwd_field.send_keys(passwd, Keys.ENTER)

# Navigating to jobs tab and searching jobs
time.sleep(1)
jobs_tab = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobs_tab.click()

# Searching jobs with user input
time.sleep(1)
job_title_field = driver.find_element(By.XPATH, "//*[contains(@id, 'jobs-search-box-keyword-id-ember')]")
job_location_field = driver.find_element(By.XPATH, value='//*[contains(@id, "jobs-search-box-location-id-ember")]')

job_title = input("Enter title, skill or company: ")
job_location = input("Enter city, state or zip code: ")

job_title_field.send_keys(job_title)
job_location_field.send_keys(job_location, Keys.ENTER)
