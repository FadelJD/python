import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype = "uint8")
radius = 150
for i in range(6):
    pic = cv2.circle(canvas, (150,150), radius, (255,255,255), 2)
    radius -= 30
cv2.imshow("Editted", pic)
cv2.waitKey(0)

image = cv2.imread("Images\Cat03.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

for i in range(639):
    for j in range(639):
        (r,g,b) = image[i,j]
        grey = 0.299*r + 0.587*g + 0.114*b
        image[i,j] = grey
cv2.imshow("BGR to Grey'd", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (340, 320), 150, 255,-1)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
