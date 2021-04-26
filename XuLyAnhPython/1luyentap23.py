'''
23  Đọc vào anh5.jpg
23a. Hiển thị ảnh I.
23b. Chuyển ảnh sang ảnh grayscale Ig. Hiển thị ảnh Ig
23c. Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen. Hiển thị ảnh Ib.
23d. Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Hiển thị ảnh Ie.
23e. Xác định các contours của ảnh Ib và vẽ đường contours lên ảnh gốc I với mầu đỏ tuyệt đối.
23g. Tính diện tích lớn nhất max_area của các contours, hiển thị giá trị này.
23h. Vẽ các contours có diện tích > max_area/5 lên ảnh gốc I với mầu vàng bgr=(0,255,255).
23i. Xác định các contours của ảnh Ib và vẽ đường contours lên ảnh gốc I với mầu đỏ tuyệt đối.
23k. Xác định các contours của ảnh Ie và vẽ đường contours lên ảnh gốc I với mầu blue tuyệt đối.
23l. Biểu diễn ảnh I sang biểu diễn mầu HSV được ảnh Ihsv. Tách kênh S được ma trận ảnh Is. Hiển thị ảnh Is.
23m. Làm trơn ảnh Is theo bộ lọc trung bình cửa sổ lân cận 3x3 được ảnh Istb. Hiển thị ảnh Istb.
23n. Nhị phân ảnh Istb theo ngưỡng Otsu được ảnh nhị phân nền đen Isb. Hiển thị ảnh Isb.
23o. Xác định các contours của ảnh Isb và vẽ các contours lên ảnh gốc với mầu Green tuyệt đối.
23p. Xác định histogram của kênh ảnh V của ảnh Ihsv. Vẽ histogram.
23q. Chỉnh độ tương phản của kênh ảnh V của Ihsv theo phương pháp cân bằng histogram và hiển thị lên màn hình ảnh kết quả.
'''

############### soạn file bai23.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
# tên biến theo đúng đề bài
I = cv2.imread("anh5.jpg")
Igoc=I.copy()
#23a
cv2.imshow('anh input',I)
#23b
Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('anh gray',Ig)
#23c
nguong_otsu, Ib = cv2.threshold(Ig,0,255, cv2.THRESH_OTSU) #nhị phân ảnh, bai2 trên classr
print(nguong_otsu)
cv2.imshow('anh nhi phan bang Otsu',Ib)
#23d
Ie=cv2.Canny(Ig,0,255)
cv2.imshow('anh bien bang Canny',Ie)
#23e
_, contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("anh co ve chu tuyen", I)
#23g
max_area=0.0
cnt_max=[]
for cnt in contours:
	if max_area < cv2.contourArea(cnt):
		max_area=cv2.contourArea(cnt)
		cnt_max=cnt
		print(max_area)
#vẽ contour có diện tích max
cv2.drawContours (I, [cnt_max], -1, (255,0,255),2)
cv2.imshow('anh co ve chu tuyen',I)
#23h
#vẽ các contours với diện tích > ngưỡng?
for cnt in contours:
	if cv2.contourArea(cnt) > max_area/5:
		cv2.drawContours(I,[cnt],-1,(0,255,255),2)

cv2.imshow("bo cac contour qua nho",I)
#23i giải ở trên
#23k màu đỏ
_, contours, _ = cv2.findContours(Ie, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #tìm Countours
cv2.drawContours (I, contours, -1, (128,0,255),2) #vẽ Contours
cv2.imshow('anh co ve chu tuyen lay tu anh bien Ie',I)
#23l
Ihsv = cv2.cvtColor(Igoc, cv2.COLOR_BGR2HSV) #chuyển sang ảnh grayscale
#tách kênh s và hiển thị
Is=Ihsv[:,:,1]
cv2.imshow("kenh S",Is)
#23m
h=Is.shape[0]
w=Is.shape[1]
Istb=cv2.blur(Is,(3,3))
cv2.imshow('anh smooth trung binh cong',Istb)
#23n
nguong_otsu,Isb = cv2.threshold(Istb,0,255,cv2.THRESH_OTSU) #nhị phân ảnh OTSU
cv2.imshow('anh nhi phan the Otsu',Isb)

#23o màu xanh
_, contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 3)
cv2.imshow("anh I voi Contours", I)
#23p
hist=cv2.calcHist([Ihsv],channels=[2],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist)
plt.show()
#23q
Ihsv[:,:,2]= cv2.equalizeHist(Ihsv[:,:,2])
cv2.imshow('anh can bang histogram kenh V', Ihsv[:,:,2])
Imoi=cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow('anh RGB can bang kenh V trong bieu dien HSV',Imoi)
###############
cv2.waitKey()
