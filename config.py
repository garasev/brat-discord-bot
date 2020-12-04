import os

TOKEN = 'NzEyMzQyMDI0ODcwODIxODg5.XsQKRQ.1rtIgw-Xbgz9gWGuJq3tbqgbcZ8'
PATH = 'D:/git/p0rn/python/bot/src'
MAX_LAVROV_CHANNEL = '769645535824183357'

songs = []
for dirpath, dirnames, filenames in os.walk(PATH):
    for file in filenames:
        if file[-4:] == '.mp3':
            songs.append(os.path.normpath(file))
print(songs)