from selenium import webdriver
import time

url = 'file:///C:/Users/Paavan%20Gopala/Downloads/Ex_Files_Python_Automation_Testing/' \
      'Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html'

driver = webdriver.Firefox()
driver.get(url)

username = driver.find_element_by_name('username')
user = driver.find_elements_by_xpath("//input[@name='username']")
print(f"My input element: {username}\n {user}")

time.sleep(1)
driver.close()
