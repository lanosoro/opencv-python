# warp

import cv2
import  numpy as np
print ("package imported")
img= cv2.imread("resources/playingcards-1140x1140-1-20150318.jpg")
pts1 = np.float32([[560,105],[1071,210],[443,843],[983,936]])
pts2 = np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix =cv2.getPerspectiveTransform(pts1,pts2)
imgOutput =cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("image",img)
cv2.imshow("image",imgOutput)
cv2.waitKey(0)