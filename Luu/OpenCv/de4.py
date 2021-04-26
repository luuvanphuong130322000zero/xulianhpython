import cv2
import numpy as np
import matplotlib as plt

#ten bien theo de bai
I = cv2.imread("anh5.jpg")
cv2.imshow("anh goc", I)

h = I.shape[0];
w = I.shape[1]
#chuyen anh mau sanh gray theo ct
#Ig = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',Ig)
Ig = np.zeros((h, w), dtype='uint8')
for i in range (h):
	for j in range (w):
		#gray = 0.39*r + 0.50*g + 0.11*b
		d = 39*int(I[i][j][2]) + 50*int(I[i][j][1]) + 11*(I[i][j][0])
		d = d//100
		Ig[i][j]=d
cv2.imshow("anh gray", Ig)
#xác định mức xám lớn nhất
print("Muc xam lon nhat",np.max(Ig))
#Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Hiển thị ảnh Ie.
Ie=cv2.Canny(Ig,0,255)
cv2.imshow('anh bien bang Canny',Ie)

#Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của  ảnh Ig theo phép dò biên Canny không? 
print("Điểm biên của ảnh Gray theo phép dò Canny",Ie[160,326])

#Nhị phân Ig theo ngưỡng otsu được Ib
nguong_otsu, Ib = cv2.threshold(Ig,0,255, cv2.THRESH_OTSU)
print("nguong: ",nguong_otsu)
cv2.imshow("anh nhi phan bang Otsu", Ib)

#Xác định các contours của ảnh Ib và vẽ đường contours lên ảnh gốc I với mầu đỏ tuyệt đối.
_,contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("anh co ve chu tuyen", I)

#Tính diện tích lớn nhất max_area của các contours, hiển thị giá trị này.
max_area=0.0
cnt_max=[]
for cnt in contours:
    if max_area < cv2.contourArea(cnt):
        max_area=cv2.contourArea(cnt)
        cnt_max=cnt
print(max_area)
#vẽ contour có diện tích max
cv2.drawContours (I, [cnt_max], -1, (255,0,255),2)  
cv2.imshow('anh co ve chu tuyen max',I) 

#Vẽ các contours có diện tích > max_area/5 lên ảnh gốc I với mầu vàng bgr=(0,255,255).
#vẽ các contours với diện tích > ngưỡng?
for cnt in contours:
    if cv2.contourArea(cnt) > max_area/5:
        cv2.drawContours(I,[cnt],-1,(0,255,255),2)
cv2.imshow("bo cac contour qua nho",I)


###############################
cv2.waitKey()