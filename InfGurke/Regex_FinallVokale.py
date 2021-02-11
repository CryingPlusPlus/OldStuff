import re

vokaleRegex = re.compile(r'[aeiuoAEIUO]')
konsonantenRegex = re.compile(r'[^aeiouAEIOU ]')

text = 'Hallo mein Name ist Ben und ich mag Eis'

vokale = vokaleRegex.findall(text)
konsonanten = konsonantenRegex.findall(text)
print(vokale)
print('')
print(konsonanten)