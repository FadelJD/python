import cv2
import numpy as np 

image = cv2.imread(r"Images\Coin.png",0)

def convolution(image):
    height = image.shape[0]
    width = image.shape[1]
    canvas = np.zeros((height, width), dtype = "uint8")
    for i in range(height-2):
        for j in range(width-2):
            y_kernel = np.array([[-1, -2, -1], 
                                 [0, 0, 0], 
                                 [1, 2, 1]])

            x_kernel = np.array([[-1, 0, 1], 
                                 [-2, 0, 2], 
                                 [-1, 0, 1]])

            gx = np.sum(np.multiply(image[i:i+3, j:j+3], x_kernel))
            gy = np.sum(np.multiply(image[i:i+3, j:j+3], y_kernel))
            total = np.sqrt(gx**2 + gy**2)
            canvas[i][j] = np.clip(total, 0, 255)
    cv2.imshow("", canvas)
    cv2.waitKey(0)

convolution(image)
 
#Task 2:

img = cv2.imread(r"Images\Coin.png",0)
pic2 = cv2.imread(r"Images\Coin.png")

img = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Blurred", img)

canny = cv2.Canny(img, 30, 150)
cv2.imshow("Canny", canny)

cnts, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
pic = cv2.drawContours(pic2, cnts, -1, (0, 0, 255), 2)

cv2.imshow("Countoured", pic )
cv2.waitKey(0)
