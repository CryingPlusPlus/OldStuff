import requests
from bs4 import BeautifulSoup

URL = 'https://www.bgbaden-frauen.ac.at/lehrer'

page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
lehrer = soup.findAll(class_='pic-title')
lehrer_email = []

for line in lehrer:
    lehrer_email.append(str(str(line).split('>')[1]).split('<')[0].lower().split(' ')[0] + '.' + str(str(line).split('>')[1]).split('<')[0].lower().split(' ')[1] + '@bildung.gv.at')

print('Wen?')
name = input()

lehrer = []
for email in lehrer_email:
    if name == str(email.split('.')[1].split('@')[0])[:name.__len__()]:
        print(email)
