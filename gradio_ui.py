import cv2 as cv 
import gradio as gr 
import numpy as np 

def convert_img(image): 
    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray_img

iface = gr.Interface(
    fn = convert_img,
    inputs = gr.Image(type = "numpy"),
    outputs = "image",
    title = "Goruntu Grilestirme", 
    description = "Goruntu Grilestirme Uygulaması"
) 

if __name__ == "__main__" : # bu dosyayı başka bir dosyadan import edip kullanmaya calisirsak izin verme sadece ana dosyaysa calistir 
    iface.launch()