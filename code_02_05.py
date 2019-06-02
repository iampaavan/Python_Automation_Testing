from selenium import webdriver
import time

url = 'file:///C:/Users/Paavan%20Gopala/Downloads/Ex_Files_Python_Automation_Testing/' \
      'Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html'

driver = webdriver.Firefox()
driver.get(url)

content = driver.find_element_by_class_name('content')
content_xpath = driver.find_elements_by_xpath("/h3[@class='content']")
print(f"My class element: {content}")
print(content_xpath)

time.sleep(2)
driver.close()
