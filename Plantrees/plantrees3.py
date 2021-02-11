from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import time, random
import pickle


driver = webdriver.Firefox()
driver.get('https://www.ecosia.org/')

with open('words.txt', 'rb') as fh:
    words = pickle.load(fh)

for word in tqdm(words):
    i0 = 0
    while 1:
        i0 += 1
        try:
            searchbar = driver.find_element_by_xpath('/html/body/div/div/div/section[1]/div[1]/form/div[1]/input')
            searchbar.send_keys(word)
            searchbar.send_keys(Keys.RETURN)

            i1 = 0
            while 1:
                i1 += 1

                try:
                    driver.find_element_by_css_selector('a.result-url').click()
                    time.sleep(random.uniform(1, 5))
                    driver.execute_script('window.history.go(-2)')
                    break
                except:
                    if i1 > 50:
                        driver.execute_script('window.history.go(-1)')
                        break
                    time.sleep(0.1)

            break
        except:
            if i0 > 50:
                break
            time.sleep(0.111)

