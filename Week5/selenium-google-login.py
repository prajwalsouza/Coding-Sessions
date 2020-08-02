from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys 

urlToUse = 'https://accounts.google.com/signin/v2/identifier?service=CPanel'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(options=options)
driver.get(urlToUse)

emailBox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@type, "email")]')))
emailBox.send_keys('codingsess@gmail.com')

time.sleep(1)
emailBox.send_keys(Keys.ENTER)

passwordBox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@type, "password")]')))
passwordBox.send_keys("somepassword")

passwordBox.send_keys(Keys.ENTER)

		
