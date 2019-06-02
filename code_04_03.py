from selenium import webdriver

url = 'http://www.python.org'

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)

my_element = driver.find_element_by_id('start-shell')

driver.close()
