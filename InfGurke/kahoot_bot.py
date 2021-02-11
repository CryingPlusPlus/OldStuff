from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get('kahoot.it')
#element = driver.find_element_by_id("passwd-id")

print(driver)
#only works with webdriver installed