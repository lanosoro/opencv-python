import cv2
import  numpy as np
print ("package imported")

cap =cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,200)
while True:
    success, img =cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
# img = cv2.imread("resources/really.jpg")
# kernel = np.ones((5,5),np.uint8)
# imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(17,17),0)
# imgCanny =cv2.Canny(img,150,200)
# imgDilation =cv2.dilate(imgCanny,kernel,iterations=1)
# imgEroded =cv2.erode(imgDilation,kernel,iterations=1)
# cv2.imshow("image",imgGray)
# cv2.imshow("blurred",imgBlur)
# cv2.imshow("canny",imgCanny)
cv2.imshow("dialation",imgDilation)
cv2.imshow("eroded",imgEroded)
cv2.waitKey(0) & 0xFF ==ord('q')