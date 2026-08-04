import qrcode
text=input("enter your name")

qr=qrcode.make(text)
filename ="qrcode.png"
qr.save(filename)
print("generated",filename)