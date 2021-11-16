import qrcode
# Data for which you want to make QR code
# Here we are using the URL of the MakeUseOf website
data = "https://het9979.github.io/Het-in.github.io/"
# File name of the QR code Image
# Change it with your desired file name
QRCodefile = "MUOQRCode.png"
# Generating the QR code
QRimage = qrcode.make(data)
# Saving image into a file
QRimage.save(QRCodefile)
