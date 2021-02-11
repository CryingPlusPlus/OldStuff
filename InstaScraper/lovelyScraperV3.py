from selenium import webdriver
import random
import pickle
import shutil
import requests
import time

class Scraper:
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.driver.get('https://www.instagram.com/')

		

		print('\nDer Scraper ist bereits kompiliert. Du kannst ihn mit scraper\n\t.fetch(dir, n_pics, know_pics_doc) Bilder aus instagramm scrapen lasse!')

	def fetch(self, saveDir, n_pics, known_pics_doc):
		with open(known_pics_doc, 'rb') as fh:
			known_pics = pickle.load(fh)
		pics = []
		name_index = len(known_pics)
		while True:
			print(len(pics))
			try:
				new_pics = [element.get_attribute('src') for element in self.driver.find_elements_by_css_selector('img.FFVAD')]

				for pic in new_pics:
					if pic not in known_pics:
						print('new')
						pics.append(pic)
						known_pics.append(pic)

						response = requests.get(pic, stream=True)
						name = saveDir + str(name_index) + '.jpg'

						with open(name, 'wb') as fh:
							shutil.copyfileobj(response.raw, fh)
							print(name)

						name_index += 1
			
				self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

			except:
				time.sleep(random.uniform(0,0.5))

			if len(pics) >= n_pics:
				break
		with open(known_pics_doc, 'wb') as fh:
			pickle.dump(known_pics_doc, fh)
		
		print('sollte gefetched haben :)')


scraper = Scraper()