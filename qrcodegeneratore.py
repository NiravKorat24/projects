import qrcode

data = "www.google.com"

qr = qrcode.make(data)

qr.save("qrcode.png")

