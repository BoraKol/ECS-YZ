import cv2 as cv 

img = cv.imread(r'goruntu-isleme\data\satranc3x3.jpg')
print(img) 

kirmizi_kare = img[200:399, :199]  ## opencv BGR olarak kullanılır
print(kirmizi_kare)

cv.imshow("Kirmizi Kare", kirmizi_kare)
cv.waitKey(0)
cv.destroyAllWindows()