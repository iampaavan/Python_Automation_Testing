from selenium import webdriver
import time

url = 'file:///C:/Users/Paavan%20Gopala/Downloads/Ex_Files_Python_Automation_Testing/' \
      'Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html'

driver = webdriver.Firefox()
driver.get(url)

login_form_absolute = driver.find_element_by_xpath('html/body/form[1]')
login_form_relative = driver.find_elements_by_xpath('//form[1]')
login_form_id = driver.find_elements_by_xpath("//form[@id='loginForm']")

print(f"My input form is: {login_form_absolute}\n {login_form_relative}\n {login_form_id}")

time.sleep(10)
driver.close()
