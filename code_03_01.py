from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'http://python.org'

driver = webdriver.Firefox()
driver.get(url)

search_bar = driver.find_element_by_name('q')
search_bar_xpath = driver.find_elements_by_xpath('//*[@id="id-search-field"]')
print(f"XPath of Search-Bar: {search_bar_xpath}")
search_bar.clear()

search_bar.send_keys('pycon')
search_bar.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()
