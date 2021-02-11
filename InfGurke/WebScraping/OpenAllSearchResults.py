import requests, bs4, webbrowser, re

search = '+'.join(input('Suchbegriff: \n').split(' '))
search = r'https://www.google.com/search?client=firefox-b-d&q=' + search
result = requests.get(search)
soup = bs4.BeautifulSoup(result.text, 'html.parser')

a = soup.select(r'(<a href="/url?q=*>)')
print(a)