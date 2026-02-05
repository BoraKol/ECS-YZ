import cv2 as cv 

img = cv.imread(r'data\kirmizi_ferrari.jpg')

b,g,r = cv.split(img)
mavi_araba = cv.merge([r,g,b])
yesil_araba = cv.merge([b,r,g])

cv.imshow("Araba", img)
cv.imshow("Mavi Araba", mavi_araba)
cv.imshow("Yesil Araba", yesil_araba)

cv.waitKey(0)
cv.destroyAllWindows()