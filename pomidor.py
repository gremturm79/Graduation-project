import pyglet
import time

time.sleep(300)
song = pyglet.media.load('C:\\mp3\\1.mp3')
song.play()
pyglet.app.run()
