import wget
import sys


def bar_progress(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()


url = 'https://s.voicecards.ru/c/15512.mp3'
filename = wget.download(url, bar=bar_progress)
print(filename)
