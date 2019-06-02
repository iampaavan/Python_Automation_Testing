from selenium import webdriver
import time
from selenium.webdriver import ActionChains

url = 'http://jqueryui.com/droppable'

driver = webdriver.Firefox()
driver.get(url)
driver.switch_to.frame(0)

action_chains = ActionChains(driver)

source = driver.find_element_by_id('draggable')
destination = driver.find_element_by_id('droppable')

action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(5)

action_chains.drag_and_drop(source, destination).perform()
time.sleep(5)

driver.close()
