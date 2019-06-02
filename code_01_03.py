from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'http://www.python.org'
driver = webdriver.Chrome()
driver.get(url)

elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()
