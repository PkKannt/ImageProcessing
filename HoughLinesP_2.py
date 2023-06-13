import cv2
import numpy as np

img = cv2.imread("BT4.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Tìm các ảnh bằng bộ lọc canny
edges =cv2.Canny(gray, 100, 200,apertureSize =3)
cv2.imshow('edges',edges)
cv2.waitKey(0)
#Cài đặt giá trị chiêu dài nhỏ hơn 30 sẽ bị loại bỏ
minLineLength =30
#Khoảng cách tối đa cho phép giữa các phân đoạn dòng là 10
maxLineGap = 10
#Tìm các phân đoạn dòng bằng houghLinesP bằng các biến số
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength, maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(150,150,255),5)

cv2.imshow('hough',img)
cv2.waitKey(0)