import cv2 as cv 

img_org = cv.imread(r'data\yesil_elma.jpg') 
img_gry = cv.imread(r'data\yesil_elma.jpg', cv.IMREAD_GRAYSCALE)

cv.imshow("Original" , img_org)
cv.imshow("Gray" , img_gry)
cv.waitKey(0)
cv.destroyAllWindows()
