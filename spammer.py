from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://web.whatsapp.com/')

output = input('Spaghetti?\n').split(' ')

for word in output:
    print(word)

while 1:
    if input('y/n\n') == 'y':
        break
    else:
        print('take you time')
field = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

for i, word in enumerate(output):
    print(str(i/len(output) * 100) + '%')
    os.system('cls')
    field.send_keys(word)
    field.send_keys(Keys.RETURN)
