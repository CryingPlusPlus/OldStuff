
import os

os.system('start 1.jpg')

while 1:
    if input('y/n\n') == 'y':
        break

os.system(r'taskkill /f /fi "imagename eq Microsoft.Photos.exe"') #beendet das foto mit einer sehr microsoftigen methode
