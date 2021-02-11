from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random

# driver = webdriver.Firefox()
# driver.get('https://www.ecosia.org/')

# words = ['chips', 'laptop']
# searchbar = driver.find_element_by_xpath('/html/body/div/div/div/section[1]/div[1]/form/div[1]/input')

# searchbar.send_keys(words[0])
# searchbar.send_keys(Keys.RETURN)

# while 1:
    # try:

        # url = driver.find_element_by_css_selector('a.result-url')
        # url.click()
        # time.sleep(random.uniform(1, 5))
        # driver.execute_script("window.history.go(-1)")
        # break
    # except:
        # time.sleep(0.3)


class EcoBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.ecosia.org/')
        self.searchbar = self.driver.find_element_by_xpath('/html/body/div/div/div/section[1]/div[1]/form/div[1]/input')
        # self.searchbar.send_keys('init')
        # self.searchbar.send_keys(Keys.RETURN)
        # self.searchbar = self.driver.find_element_by_xpath('/html/body/div[1]/div/nav[1]/div[1]/div/div[2]/div/form/div[1]/div[1]/input')
        # self.searchbar.clear()

    def clickFirstElement(self, w):
        self.searchbar.send_keys(w)
        self.searchbar.send_keys(Keys.RETURN)
        time.sleep(5)
        while 1:
            try:
                self.driver.find_element_by_css_selector('a.result-url').click()
                time.sleep(random.uniform(1, 5))
                self.driver.execute_script('window.history.go(-2)')
                break
            except:
                print('Spagehttiiiiiiiiiiiiiii')
                if input('Con? y/n') == 'y': 
                    break
                time.sleep(0.3)

    def cylce(self, wList):
        for w in wList:
            self.clickFirstElement(w)
            while 1:
                try:
                    self.searchbar = self.driver.find_element_by_xpath('/html/body/div/div/div/section[1]/div[1]/form/div[1]/input')
                    break
                except:
                    time.sleep(0.3)
                    print('Bolognese')

bot = EcoBot()
bot.cylce(['apfel', 'hund', 'birne', 'chips', 'zimt'])

