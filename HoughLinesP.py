import cv2
import numpy as np
img = cv2.imread('BT3.jpg', cv2.IMREAD_COLOR)
#Chuyen sang anh xám
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Tìm các ảnh bằng bộ lọc canny
edges =cv2.Canny(gray, 50, 200)
#Nhận biết các điểm tạo thành 1 đường
lines= cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=10, maxLineGap=250)
#Vẽ các đường tìm dc lên ảnh
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (173,255,47), 3)
#Hiển thị
cv2.imshow("Result Image", img)
cv2.waitKey(0)