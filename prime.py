file_out = open('myfile.jpg', 'rb')
file_inner = open('myinnerimage.jpg', 'wb')
msg = file_out.read()
file_inner.write(msg)
