from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

url = 'https://wiki.python.org/moin/FrontPage'

driver = webdriver.Firefox()
driver.get(url)

search_bar = driver.find_element_by_id('searchinput')
search_bar.clear()

time.sleep(2)

search_bar.send_keys('Beginner')
search_bar.send_keys(Keys.RETURN)

time.sleep(2)

select = Select(driver.find_element_by_xpath('//*/form/div/select'))

select.select_by_visible_text('Raw Text')
time.sleep(3)

driver.close()

