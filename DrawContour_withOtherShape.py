
import cv2
import numpy as np
img = cv2.imread('BT5.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
print('len(contours)', len(contours))
cnt = contours[0]
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)#ve hinh elípe chung quanh
print((x, y), (MA, ma), angle)


ellipse = cv2.fitEllipse(cnt)
 #định dạng màu cho đường ellipse
img=cv2.ellipse(img,ellipse,(0, 255, 0),2)

rect =cv2.minAreaRect(cnt)
box=cv2.boxPoints(rect)
box = np.int0(box)
img= cv2.drawContours(img, [box], 0, (0, 0, 255),2)

(x,y), radius =cv2.minEnclosingCircle(cnt)
center=(int(x),int(y))
radius=int(radius)
img=cv2.circle(img,center,radius,(0,150,255),2)

cv2.imshow('fd', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





