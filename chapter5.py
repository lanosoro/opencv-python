import cv2
import numpy as np


img = cv2.imread("Resources/Screenshot (89).png")

width,height = 750,750
pts1 = np.float32([[522,209],[949,200],[463,674],[977,681]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

gray = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgOutput,10,30,apertureSize = 3)
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(imgOutput,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow('image', imgOutput)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Image",imgOutput)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
