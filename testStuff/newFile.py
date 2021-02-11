from selenium import webdriver
from time import time

def timer(f):
    def inner():
        a = time()
        f()
        b = time()
        print('to get the page took:', b - a, 'secs')
    return inner


driver = webdriver.Firefox()
driver.get("https://www.bgbaden-frauen.ac.at/")
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div/span/a').click()
print('Hello World!')