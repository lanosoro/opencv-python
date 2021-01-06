# image resizig an croping
import cv2
import numpy as np

img =cv2.imread("resources/really.jpg")
print(img.shape)
imgResize =cv2.resize(img,(3000,200))
print(imgResize.shape)
imgCroped = img[0:200,200:500]
cv2.imshow("image",img)
cv2.imshow("image",imgResize )
cv2.imshow("image",imgCroped)
cv2.waitKey(0)