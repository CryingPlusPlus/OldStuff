# imports
from selenium import webdriver
import random
import pickle
import shutil
import requests
import time

#init driver and get Instagram
driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')

#info handling -> save and load known imgs
def getKnownPics(file):
	with open(file, 'rb') as fh:
		return pickle.load(fh)

def setKnownPics(file, kp):
	with open(file, 'wb') as fh:
		pickle.dump(kp, fh)


#main scraper kann erst gecalled werden wenn man im Browser zu dem ziel hashtag gekommen ist

def scraper(name_index, known_pics, directory, n_pics):
	input('Bist du im Zielobjekt?')
	pics = []
	error = 0
	while True:
		error += 1
		# try except... falls die Seite noch Zeit zum laden braucht
		try:
			# holt sich die source urls von den "sichtbaren" Bildern
			new_pics = [element.get_attribute('src') for element in driver.find_elements_by_css_selector('img.FFVAD')]
				# schaut für jede dieser urls ob er sie schon kennt
			for pic in new_pics:
				if pic not in known_pics:
					#wenn nicht merkt er sich dass er sie kennt
					pics.append(pic)
					known_pics.append(pic)

					#holt sich über die request bib das objekt von der url
					response = requests.get(pic, stream=True)
					name = directory + str(name_index) + '.jpg'
					# und speichert es unter einem vordefinierten Namen als jpg
					with open(name, 'wb') as fh:
						shutil.copyfileobj(response.raw, fh)
						print(name)

					name_index += 1
			# nachdem er das ganze gemacht hat srollt er eine "fensterhöhe" weiter und macht eine random pause gegen bot detection
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
			error = 0
			time.sleep(random.uniform(0, 0.5))

		except:
			time.sleep(random.uniform(0, 0.5))
			if error >= 1000:
				break

		# wenn er genug bilder gespeichert hat hört er auf
		if len(pics) >= n_pics:
			break

	print('Bitte nicht vergessen, die gefundenen Bilder mit setKnownPics() zu speichern :)\n')


#handler, damit man die Befehle in der -i Shell nicht sebst tippen muss...
def run(name_index, directory, n_pics, kp_file):
	kp = getKnownPics(kp_file)
	scraper(len(kp), kp, directory, n_pics)
	setKnownPics(kp_file, kp)