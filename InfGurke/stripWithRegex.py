import re
strip = re.compile(r'[^ \t]+')
text = '   Hello World!    '
print(' '.join(strip.findall(text)))