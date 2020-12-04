import os

TOKEN = ''
PATH = ''
MAX_LAVROV_CHANNEL = ''

songs = []
for dirpath, dirnames, filenames in os.walk(PATH):
    for file in filenames:
        if file[-4:] == '.mp3':
            songs.append(os.path.normpath(file))
print(songs)
