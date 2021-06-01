#Bu kod direkt olarak bana ait değildir. İnternetten bulduğum bir sürü kod ile yamaladım.
#Kodun işlevi bir dosya içerisindeki tüm fotoğraflara zaman etiketi koymaktır.

import time,os,datetime
from PIL import Image, ImageFont, ImageDraw
foto_konum = "" #/Users/username/... şeklinde yazın
onlyfiles = [f for f in os.listdir(foto_konum) if os.path.isfile(os.path.join(foto_konum, f))]
font = ImageFont.truetype("",150) #Buraya fontun adresini bu şekilde(/Users/username/...) yazın. Font .tff olacak. 
def tarih_bulma(path):
    return Image.open(path)._getexif()[36867]

for a in onlyfiles:
    resim = Image.open(foto_konum+a)
    donuk = resim.rotate(270,expand=True) #Fotoğraflar dönükse buradan değiştirin 270 derece
    edit = ImageDraw.Draw(donuk)
    edit.text((40,20), tarih_bulma(foto_konum+a), (255, 255, 255), font=font)
    donuk.save(""+a) #Tırnak arasına fotonun kayıt olacağı yeri yazın. /Users/username/...
    