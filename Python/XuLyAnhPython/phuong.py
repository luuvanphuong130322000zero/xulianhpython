import cv2
import numpy as np
import matplotlib.pyplot as plt
# tên biến theo đúng đề bài
I = cv2.imread("hoa1.jpg")
#cv2.imshow("Color image", I)
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV) #chuyển sang ảnh grayscale
#cv2.imshow("HSV image", Ihsv)
#HSV sang RGB (RGB đảo ngược các kênh R và B, tức là BGR)
I2 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
#cv2.imshow("RGB image", I2)
#tách kênh V
Iv=Ihsv[:,:,2]
#tách kênh H
#Ih=Ihsv[:,:,0]
#tách kênh S
Is=Ihsv[:,:,1]
#24e. Giảm size ảnh xuống 1/2. Hiển thị ảnh đã giảm size
width_I = int(I.shape[1] * 50/ 100)
height_I = int(I.shape[0] * 50 / 100)
#resize = (width, height)
# resize image
I_resize = cv2.resize(I,(width_I, height_I))
cv2.imshow("Resize image", I_resize)
#cv2.imshow('kenh H', Ih)
cv2.imshow("V image", Iv)
#Hiển thị histogram Iv
hist = cv2.calcHist ([Iv], [0],None,[256],[0,256])
plt.plot(hist)
plt.show()
'''
#Làm trơn Ihsv kênh H
Ih = cv2.medianBlur(Ihsv[:,:,0], 7) # Add median filter to image
cv2.imshow('Loc trung binh kenh H', Ih)
'''
I_h=Ihsv[:,:,0]#Kenh H
h=I_h.shape[0]
w=I_h.shape[1]
Ih=np.zeros((h,w,1),dtype='uint8')
Ih[:,:,0]=cv2.blur(I_h,(7,7))
#cv2.imshow('Loc trung binh kenh H', Ih)
#24h. Nhị phân hóa anh Ih theo ngưỡng Otsu được ảnh nhị phân Ib. Hiển thị ảnh Ib.
ret, Ib = cv2.threshold(Ih,0,255, cv2.THRESH_OTSU) 
cv2.imshow("Otsu image", Ib)
#24i. Tìm các contour của ảnh Ib. Vẽ các đường contour trên ảnh gốc I. Hiển thị ảnh I.
_, contours, _= cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#contour của ảnh Ib.#cv2.imshow("Binary image", Ib)
cv2.drawContours (I, contours, -1, (0,0,255), 3) #vẽ Contours
#cv2.imshow("Contours image", I)
#24k.Vẽ đường contour có diện tích lớn nhất ở câu 24i trên ảnh gốc I. Hiển thị ảnh I.
max_area=0.0
for cnt in contours:
    if max_area < cv2.contourArea(cnt):
        max_area=cv2.contourArea(cnt)
for cnt in contours:
    if cv2.contourArea(cnt) > max_area/2:
        cv2.drawContours(I,[cnt],-1,(0,255,255),2)

#cv2.imshow("Bo cac contour qua nho",I)
#24o  grayscale theo công thức biến đổi bộ mầu (r,g,b) về mức xám=0.39*r+0.50*g+0.11*b
rows=I.shape[0]
cols=I.shape[1]
Ig=np.zeros((rows,cols),dtype='uint8')
for i in range(rows):
    for j in range(cols):
        #gray=11*r+50*g+39*b
        d=39*int(I[i][j][2]) + 50*int(I[i][j][1]) + 11*int(I[i][j][0])
        d=d//100
        Ig[i][j]=d
cv2.imshow('Gray img:',Ig)

###############################
cv2.waitKey()