import cv2

img = cv2.imread("ISIC_0000042.jpg")
foto = cv2.resize(img, (600,600))
imgGray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
GasBlur = cv2.GaussianBlur(imgGray,(3,3),0)



imgAdp = cv2.adaptiveThreshold(GasBlur.copy(), 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,45,3)

medBlr = cv2.medianBlur(imgAdp, 3)

imPain = cv2.inpaint(foto, medBlr, 13, cv2.INPAINT_TELEA)

cv2.imshow("win", imPain)
cv2.waitKey(0)
