import qrcode

data = 'http://itrash.byethost32.com/?i=1'

file_name = 'site.png'
img = qrcode.make(data)
img.save(file_name)
