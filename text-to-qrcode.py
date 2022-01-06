import pyqrcode

code = input("Enter the message you want hidden in a QRCode: ")

qr = pyqrcode.create(code)
qr_generated = input("Enter the file name of the qr image: ")

img = qr.png(qr_generated, scale = 25)  

print("Qr code generated successfully")
print("Saved the created image in current working directory")
