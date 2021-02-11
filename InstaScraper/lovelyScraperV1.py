from selenium import webdriver
import random
import pickle
import shutil
import requests
import time

#Liste von Bildern die er kennt
with open('known_pics.txt', 'rb') as fh:
	known_pics = pickle.load(fh)

name_offset = len(known_pics)

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')

input('Login and #\n')

n_pics = int(input('Wie viele Pics?\n'))

#er speichert und scrollt, solange bis er die gewünschte anzahl an Bildquellen hat

pics = []
while True:
	#pics = pics + [element.get_attribute('src') for element in driver.find_elements_by_css_selector('img.FFVAD')]
	try:
		new_pics = [element.get_attribute('src') for element in driver.find_elements_by_css_selector('img.FFVAD')]

		for pic in new_pics:
			if pic not in known_pics:
				known_pics.append(pic)
				pics.append(pic)

		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	except:
		time.sleep(0.1)

	if len(pics) >= n_pics:
		break
'''
for i, url in enumerate(new_pics):
    response = requests.get(url, stream=True)
    name = 'picsV2/' + str(i + name_offset) + '.png'
    with open(name, 'wb') as fh:
        shutil.copyfileobj(response.raw, fh)


'''
responses = [requests.get(url, stream=True) for url in pics]
'''
with open('known_pics.txt', 'wb') as fh:
	pickle.dump(known_pics, fh)
'''

print('Sucessfull')