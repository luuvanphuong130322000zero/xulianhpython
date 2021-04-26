import cv2
import numpy as np
import matplotlib.pyplot as plt 

I=cv2.imread('2633b9cc523981edad1e11ccee5c6d31.jpg')
cv2.imshow('Anh goc:',I)

#Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Ihsv.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('Anh HSV:',Ihsv[:,:,0])
w=Ihsv.shape[1] 
h=Ihsv.shape[0] 
def tinh_his(Igray): 
	mang =np.zeros(256,dtype='uint32') 
	for i in range(h): 
	    for j in range(w): 
	        g=Igray[i][j] 
	        mang[g][0]=mang[g][0]+1 
	    return mang 
	Ir=Ihsv[:,:,2] 
	hist_r=tinh_his(Ir)
	I2 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("RGB", I2)
cv2.waitKey(0)
