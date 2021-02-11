from selenium import webdriver
import random
import pickle
import shutil
import requests

#Liste von Bildern die er kennt
with open('known_pics.txt', 'rb') as fh:
	known_pics = pickle.load(fh)

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')

input('Login and #\n')

n_pics = int(input('Wie viele Pics?\n'))

#er speichert und scrollt, solange bis er 200 Bildquellen hat
pics = []
while True:
	pics = pics + [element.get_attribute('src') for element in driver.find_elements_by_css_selector('img.FFVAD')]
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	if len(pics) >= n_pics:
		break
print('Du hast ', n_pics, ' Pics!')

new_pics = []

for pic in pics:
	if pic not in known_pics:
		known_pics.append(pic)
		new_pics.append(pic)


for i, url in enumerate(new_pics):
    response = requests.get(url, stream=True)
    name = 'picsV2/' + str(i) + '.png'
    with open(name, 'wb') as fh:
        shutil.copyfileobj(response.raw, fh)


with open('known_pics.txt', 'wb') as fh:
	pickle.dump(known_pics, fh)


print('Sucessfull')
