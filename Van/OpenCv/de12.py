import cv2
import numpy as np
import matplotlib.pyplot as plt

#cau1
I = cv2.imread('hoa1.jpg')
cv2.imshow('anh goc', I)

#cau2 
#Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
#Hiển thị kênh S của Ihsv
cv2.imshow('Anh kenh S:',Ihsv[:,:,1])

#Xác định giá trị mức sáng lớn nhất của kênh V của ảnh Ihsv
print("Muc sang lon nhat cua kenh V",np.max(Ihsv[:,:,2]))

#câu 3(12):Làm trơn ảnh kênh V của Ihsv của bộ lọc trung bình cộng, 
#kích thước cửa sổ lân cận là 3x3 được ảnh Iv. Hiển thị ảnh Iv
I_v=Ihsv[:,:,2]#Kenh V
h=I_v.shape[0]
w=I_v.shape[1]
Iv=np.zeros((h,w,1),dtype='uint8')
Iv=cv2.blur(Ihsv[:,:,2],(3,3))
cv2.imshow('anh smooth trung binh cong',Iv)



#câu4(12): nhị phân hóa ảnh Iv theo ngưỡng otsu được ảnh nhị phân Ib. hiển thị Ib
Otsu, Ib = cv2.threshold(Iv,0,255, cv2.THRESH_OTSU) 
cv2.imshow("Otsu image", Ib)



#câu 5: xác định đường contour có chu vi lớn nhất của ảnh Ib. 
#Vẽ đường contour trên ảnh gốc I và hiển thị  (câu 6(9))
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,255,255), 2)
cv2.imshow("anh co ve chu tuyen", I)

#câu 6: tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp cân bằng histogram
#Biến đổi ngược ảnh Ihvs về biểu diễn màu rbg về ảnh I. Hiển thị

Ihsv_V=cv2.equalizeHist(Ihsv[:,:,2])
cv2.imshow('Kenh V can bang histogram',Ihsv_V)

I2 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("RGB", I2)

cv2.waitKey()