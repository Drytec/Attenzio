import qrcode

url='core/sesion_online.html'
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save('qr.png')