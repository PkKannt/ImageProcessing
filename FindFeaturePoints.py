import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('Home.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=500, qualityLevel=0.05, minDistance=25)


corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img), plt.show()


