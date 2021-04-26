import cv2
import numpy as np
import matplotlib.pyplot as plt

#cau1
I = cv2.imread('hoa1.jpg')
cv2.imshow('anh goc', I)


#cau2 
#Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
#Hiển thị kênh V của Ihsv
cv2.imshow('Anh kenh V:',Ihsv[:,:,2])

#Xác định giá trị mức sáng lớn nhất của kênh S của ảnh Ihsv
print("Muc sang lon nhat cua kenh S",np.max(Ihsv[:,:,1]))
#Xác định giá trị mức sáng nhỏ nhất của kênh S của ảnh Ihsv
print("Muc sang lon nhat cua kenh S",np.max(Ihsv[:,:,1]))

#Câu 3(9): Xác định và vẽ histogram của kên v của ảnh Ihsv

hist=cv2.calcHist([Ihsv],channels=[2],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist)
plt.show()

#câu4(9): Làm trơn theo bộ lọc median Is
Is = cv2.medianBlur(Ihsv[:,:,1], 3) # Add median filter to image
cv2.imshow('Loc trung binh kenh S', Is)

#câu5: nhị phân hóa ảnh Is theo ngưỡng otsu được ảnh nhị phân Ib. hiển thị Ib
Otsu, Ib = cv2.threshold(Is,0,255, cv2.THRESH_OTSU) 
cv2.imshow("Otsu image", Ib)

#câu 6: xác định đường contour có chu vi lớn nhất của ảnh Ib. 
#Vẽ đường contour trên ảnh gốc I và hiển thị  (câu 6(9))
_, contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("anh co ve chu tuyen", I)

cv2.waitKey()
