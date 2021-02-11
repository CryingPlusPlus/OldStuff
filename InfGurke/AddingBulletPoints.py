import pyperclip

bullets = str(pyperclip.paste())

bullets = bullets.split('\n')
bullets = ''.join(bullets).split('\r')
del(bullets[-1])
end = []
for p in bullets:
    end.append('* ' + p)
print('\n'.join(end))
pyperclip.copy('\n'.join(end))