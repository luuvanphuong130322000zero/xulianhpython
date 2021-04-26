import cv2
import numpy as np
#Cau 1:
img = cv2.imread("2633b9cc523981edad1e11ccee5c6d31.jpg")
cv2.imshow("Anh goc", img)
#Cau 2:
(h, w, d) = img.shape
new_img = np.zeros((h,w,1),dtype='uint8')
print("Height={}, Width={}, Depth={}".format(h, w, d))
for i in range(h):
    for j in range(w):
        r, g, b = img[i, j]
        avg = r * 39 + g *50 + b * 11
        avg = avg // 100
        new_img[i, j] = avg
cv2.imshow("Anh xam", new_img)
#Cau 3:
def scale_to_0_255(img):
    min_val = np.min(img)
    max_val = np.max(img)
    new_img = (img - min_val) / (max_val - min_val) # 0-1
    new_img *= 255
    return new_img

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

cv2.imshow("Sobelx", sobelx)
cv2.imshow("Sobely", sobely)

sobelx = scale_to_0_255(sobelx)
sobely = scale_to_0_255(sobely)

cv2.imwrite("Sobelx sau khi scale.jpg", sobelx)
cv2.imwrite("Sobely sau khi scale.jpg", sobely)
#Cau 4:
img_canny = cv2.Canny(new_img, 0, 255)
cv2.imshow("Canny image", img_canny)
#Cau 5:

cv2.waitKey()