import cv2
image = cv2.imread(r"Images\Coin.png", cv2.IMREAD_GRAYSCALE)
fngrprint = cv2.imread(r"Images\fingerprint.png", cv2.IMREAD_GRAYSCALE)
def BasicTh(img):
    img2 = img
    x,y = img.shape[0],img.shape[1]
    th = 71 if x > 500 else 127
    for i in range(x):
        for j in range(y):
            if img[i,j] < th:
                img2[i,j] = 255
            else:
                img2[i,j] = 0
    cv2.imshow("Thresholded", img2)
    cv2.waitKey(0)
BasicTh(fngrprint)
BasicTh(image)