import pyscreenshot

img = pyscreenshot.grab(bbox=(10, 10, 510, 510))
img.show()

img.save('myimage.png')