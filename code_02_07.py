from selenium import webdriver
import time

url = 'http://www.seleniumhq.org/'

driver = webdriver.Firefox()
driver.get(url)

element_id = driver.find_element_by_id('q')
print(f"Element by ID: {element_id}")

element_name = driver.find_element_by_name('q')
print(f"Element by Name: {element_name}")

heading_xpath = driver.find_elements_by_xpath('//*[@id="mainContent"]/h2[1]')
#heading_xpath_1 = driver.find_elements_by_xpath('//h2[1][1]')
#print(heading_xpath_1)
print(f"Heading XPath:{heading_xpath}")

element_class = driver.find_elements_by_class_name('selenium-sponsors')
print(f"Element Class Name: {element_class}")

time.sleep(5)
driver.close()
