import cv2
img=cv2.imread("BT1.png")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# phân ngưỡng ảnh xám
ret, thresh=cv2.threshold(gray,127,255,0)
# Tìm đường viền của ảnh với 3 đối số
# ( ảnh , truy xuất đường viền và lấy xấp xỉ đường thẳng đó)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
M= cv2.moments(thresh)     #Tính điểm trọng tâm
cX= int(M["m10"] / M["m00"])
cY= int(M["m01"] / M["m00"])
cv2.circle(img,(cX,cY), 5, (255, 255, 255),-1) # Xác định màu của tọa độ đánh dấu
cv2.drawContours(img, contours, 1, (0 , 255, 0), 3)
cv2.putText(img, "centroid", (cX-25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 255, 0, 255), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)