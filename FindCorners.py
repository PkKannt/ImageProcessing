import cv2
import numpy as np

def detect_corner(image_path, blockSize=2, ksize=3, k=0.04, threshold=0.01):

    img = cv2.imread('Home.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, blockSize, ksize, k)
    # kết quả là giãn ra để đánh dấu các góc không quan trọng
    dst = cv2.dilate(dst, None)
    # Ngưỡng cho một giá trị tối ưu, nó có thể khác nhau tùy thuộc vào hình ảnh.
    img[dst > threshold * dst.max()] = [0, 0, 255]
    cv2.imwrite('example_Corners.png', img)

    return img
temp= detect_corner(cv2.imread('home2.png'), blockSize=2, ksize=3, k=0.04, threshold=0.01)
cv2.imshow("temp",temp)
cv2.waitKey(0)
