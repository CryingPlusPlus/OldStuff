from pytube import YouTube
import pyperclip

while True:
    a = input('Link in Clipboard? (y/n)')
    if a == 'y':
        break
    if a == 'n':
        print('then copy it\n')
    else:
        print('not a valid input')

link = pyperclip.paste()
#link1 = 'https://youtu.be/' + link.split('=')[1]
#YouTube(link1).streams.get_highest_resolution().download()

#YouTube(link).streams.get_highest_resolution().download()

#yt = YouTube(link)
#yt.streams.filter(file_extension='mp4').order_by('resolution')[-1].download()

