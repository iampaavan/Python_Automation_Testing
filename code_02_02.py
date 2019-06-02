from selenium import webdriver
import time

url = 'file:///C:/Users/Paavan%20Gopala/Downloads/Ex_Files_Python_Automation_Testing/' \
      'Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html'

driver = webdriver.Firefox()
driver.get(url)

login_form = driver.find_element_by_id('loginForm')
print(f"My login form element is: {login_form}")

time.sleep(10)
driver.close()
