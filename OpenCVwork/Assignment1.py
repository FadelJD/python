import cv2

image = cv2.imread("Images\sunset_image.png")
(b, g, r) = image[0,0]
print('Pixel at (0,0) Red : {} Green : {} Blue : {}'.format(r,g,b))
# get dimensions of image
dimensions = image.shape
image2 = image
image3 = image
image4 = image
height = image.shape[0]
width = image.shape[1]
image[0:height//2, 0:width//2, 0] = 0   #green
image2[height//2:, width//2:, 1] = 0    #red
image3[0:height//2, width//2:, 2] = 0   #blue
image4[0:height//2, :width//2, 2] = 0
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

 