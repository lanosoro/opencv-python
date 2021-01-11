import cv2
import numpy as np
# shapes and texts
img=np.zeros((512,512,3),np.uint8)
# print(img)
# img[:]=255,0,0

print(img.shape)
cv2.line(img,(0,0),(300,300),(0,255,255),2)
cv2.rectangle(img,(0,0) ,(250,300),(0,255,0),2, )
cv2.circle(img,(400,50),30,(255,255,0),5 )
cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
cv2.imshow("image",img)
cv2.waitKey(0)