from pytube import YouTube
from pytube.cli import on_progress
import pytube.request
import random
import time

pytube.request.default_range_size = 5000000


def typewrite(num1, num2, text):
    for c in text:
        r = random.uniform(num1, num2)
        time.sleep(r)
        print(c, end='', flush=True)


def completed():
    completed = '\nDownload completed\n'
    size = 'File size' + str(stream.filesize / 1000000) + 'Mb\n'
    title = 'Title: ' + stream.title + '\n'
    desc = 'Description: ' + yt.description + '\n'
    author = 'Author: ' + yt.author + '\n'
    length = 'Video Length: ' + str(yt.length) + 'Seconds\n'

    lst = [completed, size, title, desc, author, length]
    for t in lst:
        typewrite(.05, .1, t)
        print('-' * 60)


url = input('\nPlease enter URL -> ')
try:
    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=completed)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    typewrite(.05, .1, 'Download is starting ...\n')
    stream.download()

except Exception as e:
    print(e)


