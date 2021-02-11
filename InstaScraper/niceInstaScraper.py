import os
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
driver.get('https://www.instagram.com/explore/tags/girls/?hl=de')

cmds = [
        # 'driver.find_element_by_xpath(\'/html/body/div[2]/div/div/div/div[2]/button[1]\').click()',
        # 'driver.find_element_by_xpath(\'/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div/div/div[3]/div[1]/a\').click()',
        # 'driver.find_element_by_xpath(\'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input\').send_keys(\'swernigge123@gmail.com\')',
        # 'driver.find_element_by_xpath(\'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input\').send_keys(\'FroscH13#\')',
        # 'driver.find_element_by_xpath(\'/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button\').click()',
        # 'driver.find_element_by_xpath(\'/html/body/div[4]/div/div/div/div[3]/button[2]\').click()',
        # 'driver.find_element_by_xpath(\'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input\').send_keys(\'#girls\')',
        # 'driver.find_element_by_xpath(\'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]\').click()',
        'print(\'HelloWorld\')',
        'print(\'HelloMoin\')',
        'print(\'moinmoin\')'
        ]

def evaCMD(cmd):
    cmd = 'def func():\n    ' + cmd
    with open('temp.py', 'w') as temp:
        temp.write(cmd)
    try:
        reload(temp)
    except:
        pass
    from temp import func
    func()
    os.system('del temp.py')
    del func
    
for cmd in cmds:
    i = 0
    while 1:
        i += 1
        try:
            evaCMD(cmd)
            break
        except:
            time.sleep(0.1)
            print('waiting for response', i)


