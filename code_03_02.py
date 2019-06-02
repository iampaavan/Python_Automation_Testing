from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

url = 'file:///C:/Users/Paavan%20Gopala/Downloads/Ex_Files_Python_Automation_Testing/' \
      'Ex_Files_Python_Automation_Testing/Exercise%20Files/CH03/03_02/html_code_03_02.html?' \
      'numReturnSelect=800&continue=Submit'

driver = webdriver.Firefox()
driver.get(url)

select = Select(driver.find_element_by_name('numReturnSelect'))

select.select_by_index(4)
time.sleep(3)

select.select_by_visible_text('200')
time.sleep(3)

select.select_by_value('250')
time.sleep(3)

options = select.options
print(options)

submit = driver.find_element_by_name('continue')
submit.submit()
time.sleep(3)

driver.close()

