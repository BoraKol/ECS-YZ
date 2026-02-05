import cv2 as cv

img = cv.imread(r'goruntu-isleme\data\yesil_elma.jpg')
print("yükseklik: ",img.shape[0])
print("genislik: ",img.shape[1])
print("kanal sayisi: ",img.shape[2])
print("piksel sayisi: ", img.shape[0]*img.shape[1])
print("Veri turu: ", img.dtype)