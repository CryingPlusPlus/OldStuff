from selenium import webdriver
import random
import pickle
import shutil
import requests
import time

#Liste von Bildern die er kennt
with open('known_pics.txt', 'rb') as fh:
	known_pics = pickle.load(fh)

#name_offset = len(known_pics)

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')

input('Login and #\n')

n_pics = int(input('Wie viele Pics?\n'))

#er speichert und scrollt, solange bis er die gewünschte anzahl an Bildquellen hat

pics = []
name_index = len(known_pics)
while True:
	try:
		new_pics = [element.get_attribute('src') for element in driver.find_elements_by_css_selector('img.FFVAD')]

		for pic in new_pics:
			if pic not in known_pics:
				pics.append(pic)
				known_pics.append(pic)

				response = requests.get(pic, stream=True)
				name = 'picsV2/' + str(name_index) + '.jpg'

				with open(name, 'wb') as fh:
					shutil.copyfileobj(response.raw, fh)
					print(name)

				name_index += 1
		
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

	except:
		time.sleep(0.1)

	if len(pics) >= n_pics:
		break

with open('known_pics.txt', 'wb') as fh:
	pickle.dump(known_pics, fh)


print('Sucessfull')