#QR-Code Generator
#Edit By. Dr.Rafeek Yanni
#-------------------2024-2025------------------


#---------------- Import Librarys ------------------#
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import  Image

#----------------- Start Generate QR Logo---------------------------#
qr = pyqrcode.create("Add Web Site Link")
qr.png("Weblink.png", scale=8, module_color=[0, 102, 153, 128])
rmty = decode(Image.open("Weblink.png"))

qr = pyqrcode.create("Add Facebook Page Link")
qr.png("Facebook_Page.png", scale=8, module_color=[0, 102, 153, 128])
rmty = decode(Image.open("Facebook_Page.png"))

qr = pyqrcode.create("Add Location Map Link")
qr.png("Map_Location.png", scale=8, module_color=[0, 102, 153, 128])
rmty = decode(Image.open("Map_Location.png"))

qr = pyqrcode.create("Add Whatsapp Link")
qr.png("Whatsapp.png", scale=8)
rmty = decode(Image.open("Whatsapp.png"))

print(rmty[0].data.decode("ascii"))