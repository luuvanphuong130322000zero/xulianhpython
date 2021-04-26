import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread('hoa1.jpg')
cv2.imshow('anh goc', I)

#cau1
so_cot = I.shape[1]
so_dong = I.shape[0]
print("Do cao =",so_cot)
print("Do rong =",so_dong)
print("Ty le do cao/do rong =",so_cot/so_dong)

#cau2
I2 = cv2.resize(I,(256, 256))
cv2.imshow('anh rut gon', I2)

#cau3
def tinh_hist(I):
   w=I.shape[1]
   h=I.shape[0]
   ahis=np.zeros(256,dtype='int')
   for i in range(h):
      for j in range(w):
         g=I[i][j]
         ahis[g]= ahis[g]+1
   return ahis
Ihsv= cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
Ihsv_S=tinh_hist(Ihsv[:,:,1])
# ảnh nhị phân bgr
cv2.imshow('anh kenh S cua Ihsv', Ihsv[:,:,1]) 

#cau4
I3 = cv2.cvtColor(Ihsv,cv2.COLOR_HSV2RGB)
cv2.imshow('anh I3',I3)

#cau5
Ihsv_V=Ihsv[:,:,2]
Ivb=cv2.Canny(Ihsv_V,0,255)
cv2.imshow('anh Ivb',Ivb)

#cau6
print('histogram kenh S= ', Ihsv_S)
plt.plot(Ihsv_S)

cv2.waitKey()