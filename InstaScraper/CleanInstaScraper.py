from selenium import webdriver
import requests
import shutil
import random
import time

from funcStorage import funcStorage

# driver = webdriver.Firefox()
# driver.get('https://www.instagram.com/explore/tags/girls/?hl=de')


# driver = webdriver.Firefox()

stmts = [
'driver.get(\'https://www.instagram.com/explore/tags/girls/?hl=de\')',
'driver.find_element_by_xpath(\'/html/body/div[2]/div/div/div/div[2]/button[1]\').click()',
        # 'driver.find_element_by_xpath(\'/html/body/div[2]/div/div/div/div[2]/button[1]\').click()',
        'driver.find_element_by_xpath(\'/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div/div/div[3]/div[1]/a\').click()',
        'driver.find_element_by_xpath(\'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input\').send_keys(\'swernigge123@gmail.com\')',
        'driver.find_element_by_xpath(\'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input\').send_keys(\'FroscH13#\')',
        'driver.find_element_by_xpath(\'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button\').click()',
        'driver.find_element_by_xpath(\'/html/body/div[4]/div/div/div/div[3]/button[2]\').click()',
        'driver.find_element_by_xpath(\'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input\').send_keys(\'#girls\')',
        'driver.find_element_by_xpath(\'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]\').click()',
        'input(\'y/n\')',
        'return [link.get_attribute(\'src\') for link in driver.find_elements_by_css_selector(\'.FFVAD\')]',
        # 'print(a)'
        
        # 'print(\'Hello\')',
        # 'print(\'Moin\')'

# 'driver = webdriver.Firefox()',
        ]

fS = funcStorage(stmts, 'from selenium import webdriver\nimport time\nimport urllib\ndriver = webdriver.Firefox()\n\na = None\n')
fS.initStorage()
return_List = []
for i in range(fS.n_funcs):
    t = 0
    while 1:
        try:
            a = fS.aFunc(i)
            return_List.append(a)
            break
        except:
            print('='*t)
            t += 1
            time.sleep(0.3)
    # fS.aFunc(i)

# a = driver.find_elements_by_css_selector('.FFVAD')
# print(fS.temp.a) #problem -> this file cant access a in temp needs other import (?) ... change fS.die() (?)
urls = return_List[-1]
for i, url in enumerate(urls):
    response = requests.get(url, stream=True)
    name = 'pics/' + str(i) + '.png'
    with open(name, 'wb') as fh:
        shutil.copyfileobj(response.raw, fh)

print('finished')
