from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from tqdm import tqdm
import time, random, pickle 

class Driver():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.ecosia.org/')
        self.searchbar = None
        self.ad = None


    def getSearchbar(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/div/section[1]/div[1]/form/div[1]/input')

    # def search(self, word):
        # searchbar = self.getSearchbar()
        # searchbar.send_keys(word)
        # searchbar.send_keys(Keys.RETURN)

        # while 1:
            # try:
                # ad = self.driver.find_element_by_css_selector('a.result-url').click()
                # break
            # except:
                # print('sleeping')
                # time.sleep(0.1)

        # time.sleep(random.uniform(1, 5))
        # self.driver.execute_script('window.history.go(-2)')


class Controler:
    def __init__(self, n):
        self.n = n
        self.points = 0
        self.drivers = self.initDrivers(self.n)

    def initDrivers(self, n):
        return [Driver() for i in range(n)]

    def search(self, word):
        for d in self.drivers:
            wait = 0
            while 1:
                wait += 1
                try:
                    d.searchbar = d.getSearchbar()
                    d.searchbar.send_keys(word)
                    d.searchbar.send_keys(Keys.RETURN)
                    break
                except:
                    if wait > 75:
                        break
                    time.sleep(0.1)

        for d in self.drivers:
            wait = 0
            while 1:
                wait += 1
                try:
                    d.driver.find_element_by_css_selector('a.result-url').click() 
                    break
                except:
                    if wait > 75:
                        break
                    time.sleep(0.1)
        time.sleep(random.uniform(1, 5))
        for d in self.drivers:
            d.driver.execute_script('window.history.go(-2)')
            self.points += 1
            
        return self.points 
    def die(self):
        for d in self.drivers:
            d.driver.close()
# Cont = Controler(2)
# Cont.search('chips')
# words = ['apfel', 'chips', 'zimt', 'Avocados', 'BrokkoliV']

with open('words.txt', 'rb') as fh:
    words = pickle.load(fh)

cont = Controler(3)
for word in tqdm(words):
    newTreePoints = cont.search(word)
cont.die()
with open('treePoints.txt', 'rb') as fh:
    treePoints = pickle.load(fh)
with open('treePoints.txt', 'wb') as fh:
    pickle.dump(newTreePoints + treePoints, fh)
print('total', newTreePoints + treePoints)
print('new', newTreePoints)
