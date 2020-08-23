from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys 

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Most import above aren't necessary. But, kinda useful sometimes. 

urlToVisit = 'https://youtube.com'

options = Options()
options.headless = True

# driver = webdriver.Chrome(options=options)	# Uncomment this line and comment the next, if you do not want a browser window displayed.
driver = webdriver.Chrome()
driver.get(urlToVisit)


# The following line waits for 20 seconds for the HTML element "input" with attribute "placeholder = search" to be present.  
searchBox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Search")]')))
searchBox.send_keys('LabPadre')

# If you want to wait for visibility of the element use, EC.visibility_of_element_located
time.sleep(2)

searchBox.send_keys(Keys.ENTER)

videoTitle = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@title, "LabPadre At SpaceX Boca Chica Facility Live 24/7")]')))
time.sleep(2)

videoTitle.click()

while True:
	countDiv = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@id, "info-text")]')))
	print(countDiv.text)
	time.sleep(2)
