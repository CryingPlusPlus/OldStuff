import re

text = '1  2  3 num num three'

numRegex = re.compile(r'( )?\d ')

mo = numRegex.search(text)

print(mo.groups())