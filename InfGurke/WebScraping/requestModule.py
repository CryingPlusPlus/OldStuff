import requests

stuff = requests.get('http://www.bgbaden-frauen.ac.at/~infsalzig/Ben/gewusel/Obstladen/obst')
print(stuff.text)