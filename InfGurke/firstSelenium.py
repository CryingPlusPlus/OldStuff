from selenium import webdriver
import time
import random

gamepin = input('GamePin?\n')
anzahl = input('Nickname\n')
browser = webdriver.Firefox()
# print(type(browser))
url = 'https://kahoot.it/'
browser.get(url)
form = browser.find_element_by_css_selector('input#game-input')
button = browser.find_element_by_css_selector('button.enter-button__EnterButton-sc-1o9b9va-0')
# print(type(form))
form.send_keys(gamepin)
button.click()
while True:
    try:
        nicknameform = browser.find_element_by_id('nickname')
        button = browser.find_element_by_css_selector('button')
        nicknameform.send_keys(anzahl)
        button.click()
        break
    except:
        continue
# getwebsiteinfo get string with game name search answers
print(str(browser.application_cache))
while True:
    try:
        button = browser.find_elements_by_css_selector('button.card-button__CardButton-vbewcy-2')
        random.choice(button).click()
        print('Clicked')
    except:
        print('NichtGefunden')
    time.sleep(3)
# browser.quit()
# button#kxpxeu
# <button data-functional-selector="answer answer-0" role="button" class="card-button__CardButton-vbewcy-2 llRDBo flat-button__FlatButton-sc-6uljam-0 bbSHdR"><span class="card-button__Icon-vbewcy-0 bjVMMD icon__Icon-xvsbpg-0 koWGCK" style="display: inline-block; vertical-align: middle; width: 15.75vmin; height: 15.75vmin;"><svg data-functional-selector="icon" viewBox="0 0 32 32" focusable="false"><title id="triangle-buttonTitle">Triangle button</title><desc id="triangle-buttonDesc">Triangle answer button</desc><path style="fill: rgb(255, 255, 255);" d="M27,24.559972 L5,24.559972 L16,7 L27,24.559972 Z"></path></svg></span></button>
