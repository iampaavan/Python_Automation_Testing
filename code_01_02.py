from selenium import webdriver
import time

url = 'http://www.seleniumhq.org'
browser = webdriver.Firefox()
browser.get(url)
time.sleep(10)
browser.close()

