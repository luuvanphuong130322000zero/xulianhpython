import cv2
import matplotlib.pylab as plt
import numpy as np
# đọc ảnh
img = cv2.imread('2633b9cc523981edad1e11ccee5c6d31.jpg')
cv2.imshow("anh I",img)

# tách ảnh
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, s, v = cv2.split(hsv_image)
#r, g, b = cv2.split(rgb_image)
 

#cv2.imshow('kenh v',s)
print("Muc xam lon nhat",np.max(s))
print("Muc xam nho nhat",np.min(s))

#h: vùng màu,  s: độ bão hòa,    v: độ sáng
#hiển thị kênh h, s, v
cv2.imshow("Day la anh h",h)
cv2.imshow("Day la anh s",s)
cv2.imshow("Day la anh v",v)
#cv2.imshow("Day la anh r",r)
#cv2.imshow("Day la anh g",g)
#cv2.imshow("Day la anh b",b)

# vẽ histogram kênh V
#plt.hist(v.ravel(),bins = 256, range = [0,256])
#plt.show()

# làm trơn kênh V theo median, resize ảnh 3x3
#Is = cv2.medianBlur(img, 3)
#Is = cv2.resize(Is, (500,500))
#cv2.imshow('Is',Is)



# nhị phân theo ngưỡng otsu
#row = hsv_image.shape[0]
#cols = hsv_image.shape[1]
#Ig = np.zeros((row, cols), dtype='uint8')
#for i in range(row):
#     for j in range(cols):
#         d = 255 - int(hsv_image[i][j][1])
#         Ig[i][j] = d
#a, anh = cv2.threshold(Ig, 125, 255, cv2.THRESH_OTSU)
#cv2.imshow('anh', anh)



# vẽ viền ( Contour)

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
# contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
# cv2.drawContours(gray, contours, -1, (0, 255, 0), 3)
# for contour in contours:
#     cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

#     cnt = contours[0]
#     area = cv2.contourArea(cnt)

# print('area of contour 0: {}'.format(area))
# cv2.imshow('image', img)
# cv2.waitKey(0)


# cv2.imshow('image', img)
# cv2.waitKey(0)

# cv2.waitKey(0)

# imgCanny = cv2.Canny(img, 100, 200)
# contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# cnt = contours[0]

# perimeter = cv2.arcLength(cnt,True)
# area = cv2.contourArea(cnt)

# print(perimeter)
# print(area)
# cv2.imshow('image', img)



img_blur = cv2.blur(img, ksize = (5, 5))
gradian_blur = cv2.GaussianBlur(img, ksize = (5, 5), sigmaX = 4, sigmaY=4)
cv2.imshow("Lam mo", img_blur)
cv2.imshow("Gaussian blur", gradian_blur)
cv2.waitKey(0)