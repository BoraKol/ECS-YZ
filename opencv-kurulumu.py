# Python Sanal Ortamı Kurulumu ve Genel terminal komutlarla ilgili hatırlatmalar:

# 1.yol
# pip install venv
# python -m venv <klasor adı> koduyla da sanal ortamda çalışabiliriz 

# 2.yol
# ctrl + shift + p => select interpreter => create new environment => venv

# Ek Bilgiler: 
# cd <klasor adı>\Scripts\activate ile sanal ortamı aktiflestir
# pip freeze > requirements.txt mevcut olan tum paketleri requirements.txt dosyasına yazar 
# pip install -r requirements.txt requirements.txt dosyasındaki paketleri kurar
# pip install pipregs gerekli olan tum paketleri(kutuphaneleri) kurar
# pipregs .

# sanal ortamı kapatmak için de cd <klasor adı>\Scripts\deactivate

import cv2 as cv 
print("OpenCV version: ",cv.__version__)
