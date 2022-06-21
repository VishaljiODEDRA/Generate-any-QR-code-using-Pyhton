from ensurepip import version
from turtle import fillcolor
#author:RAVI PARMAR
import qrcode   
from PIL import Image 

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4) #for formating and correction error

qr.add_data("https://www.instagram.com/mr.flame17_10/?hl=en") #for what you put in your qr code data
qr.make(fit=True)       #for what you put in your qr code data
img=qr.make_image(fill_color="blue",back_color="yellow") #for Qr color and QR backgaround color
img.save("Qr2.png") #to save the qr code