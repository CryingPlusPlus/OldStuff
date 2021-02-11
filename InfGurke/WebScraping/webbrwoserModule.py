import webbrowser, pyperclip
url = 'https://www.google.at/maps/place/' + pyperclip.paste()
webbrowser.open(url)