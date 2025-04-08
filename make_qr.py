import qrcode

with open("signed.asc", "r", encoding="utf-8") as f:
    data = f.read()

img = qrcode.make(data)
img.save("signed_qr.png")
