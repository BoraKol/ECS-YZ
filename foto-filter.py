import cv2 as cv
import numpy as np
import gradio as gr

# Farklı filtre fonksiyonları
def apply_gaussian_blur(frame):
    return cv.GaussianBlur(frame, (15, 15), 0)

def apply_box_blur(frame): 
    return cv.blur(frame, (5,5))

def apply_hsv(frame): 
    return cv.cvtColor(frame, cv.COLOR_BGR2HSV)

def apply_scale_contrast(frame):
    return cv.convertScaleAbs(frame , alpha = 1.5 , beta = 0)

def apply_sharpening_filter(frame):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, 1, 0]])
    return cv.filter2D(frame, -1, kernel)

def apply_emboss_filter(frame):
    kernel = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
    return cv.filter2D(frame, -1, kernel)

def apply_edge_detection(frame):
    return cv.Canny(frame, 100, 200)

def apply_invert_filter(frame):
    return cv.bitwise_not(frame)

def adjust_brightness_contrast(frame, alpha=1.0, beta=50):
    return cv.convertScaleAbs(frame, alpha=alpha, beta=beta)

def apply_grayscale_filter(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

# Filtre uygulama fonksiyonu
def apply_filter(filter_type, input_image=None):
    if input_image is not None:
        frame = input_image
    else:
        cap = cv.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            return "Web kameradan görüntü alınamadı"

    if filter_type == "Gaussian Blur":
        return apply_gaussian_blur(frame)
    elif filter_type == "Box Blur":
        return apply_box_blur(frame)
    elif filter_type == "HSV": 
        return apply_hsv(frame)
    elif filter_type == "Scale Contrast": 
        return apply_scale_contrast(frame)
    elif filter_type == "Emboss Filter":
        return apply_emboss_filter(frame)
    elif filter_type == "Sharpen":
        return apply_sharpening_filter(frame)
    elif filter_type == "Edge Detection":
        return apply_edge_detection(frame)
    elif filter_type == "Invert":
        return apply_invert_filter(frame)
    elif filter_type == "Brightness":
        return adjust_brightness_contrast(frame, alpha=1.0, beta=50)
    elif filter_type == "Grayscale":
        return apply_grayscale_filter(frame)

# Gradio arayüzü
with gr.Blocks() as demo:
    gr.Markdown("# Web Kameradan Canlı Filtreleme")

    # Filtre seçenekleri
    filter_type = gr.Dropdown(
        label="Filtre Seçin",
        choices=["Gaussian Blur", "Sharpen", "Edge Detection", "Invert", "Brightness", "Grayscale", "Box Blur", "HSV", "Scale Contrast", "Emboss Filter"],
        value="Gaussian Blur"
    )

    # Görüntü yükleme alanı
    input_image = gr.Image(label="Resim Yükle", type="numpy")

    # Çıktı için görüntü
    output_image = gr.Image(label="Filtre Uygulandı")

    # Görüntü yüklendiğinde filtre uygulama fonksiyonu
    input_image.change(fn=apply_filter, inputs=[filter_type, input_image], outputs=output_image)

# Gradio arayüzünü başlat
demo.launch()
