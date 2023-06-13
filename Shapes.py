import cv2
# Đọc ảnh
img = cv2.imread('BT2.png')

# Phân ngưỡng xám cho ảnh
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Cài đặc threshold cho ảnh xám
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Tìm đường viền của ảnh với 3 đối số
# ( ảnh , truy xuất đường viền và lấy xấp xỉ đường thẳng đó)
contours, _ = cv2.findContours(    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
# Tạo danh sách lưu tên các hình dạng trong ảnh
for contour in contours:

    # bỏ qua bộ đếm đầu tiên vì chức năng findcontour
    # phát hiện toàn bộ hình ảnh dưới dạng hình dạng
    if i == 0:
        i = 1
        continue
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(        contour, 0.01 * cv2.arcLength(contour, True), True)
#Lam thẳng Contours
    # Sử dụng drawContours() To viền cho các hình dạng
    cv2.drawContours(img, [contour], 0, (255, 255, 0), 5)

    # Tìm điểm trung tậm của các hình dạng
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

    # Đặt tên tại trung tâm các hình dạng
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    elif len(approx) == 4:
        cv2.putText(img, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    else:
        cv2.putText(img, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# hiển thị hình ảnh sau khi vẽ đường viền
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

