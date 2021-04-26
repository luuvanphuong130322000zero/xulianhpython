import cv2
import numpy as np

img = cv2.imread("2633b9cc523981edad1e11ccee5c6d31.jpg")
(h, w, d) = img.shape
new_img = np.zeros((h, w), dtype='uint8')
for i in range(h):
    for j in range(w):
        r, b, g = img[i, j]
        avg = r * 39 + g * 50 + b * 11
        avg = avg // 100
        new_img[i, j] = avg
retval, thresh = cv2.threshold(new_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Phan nguong otsu", thresh)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,0,255), 2)
cv2.imshow("anh co ve chu tuyen", img)
cv2.waitKey()