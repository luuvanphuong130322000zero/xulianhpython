import cv2
import numpy as np
import matplotlib.pyplot as plt 

I = cv2.imread("hoa1.jpg")
cv2.imshow("anh goc", I)

h = I.shape[0]
w = I.shape[1]
#Ig = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',Ig)
#2: ảnh 3 kênh chuyển sang 1 kênh xám theo công thức
Ig = np.zeros((h, w), dtype='uint8')
for i in range (h):
	for j in range (w):
		#gray = 0.39*r + 0.50*g + 0.11*b
		d = 39*int(I[i][j][2]) + 50*int(I[i][j][1]) + 11*(I[i][j][0])
		d = d//100
		Ig[i][j]=d
cv2.imshow("anh gray", Ig)
print("Muc xam lon nhat",np.max(Ig))
#3
#sobel

sobelx = cv2.Sobel(Ig,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(Ig,cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(Ig,cmap = 'gray')
plt.title('Ảnh gốc'), plt.xticks([]), plt.yticks([])
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

G = np.zeros((h, w), dtype= 'float64')
for i in range (h):
	for j in range (w):
		t1 = sobelx[i][j]*sobelx[i][j]
		t2 = sobely[i][j]*sobely[i][j]
		G[i][j]= np.sqrt(t1+t2)
#4: Tình Canny
Ie=cv2.Canny(Ig,0,255)
cv2.imshow('anh bien bang Canny',Ie)
#print("Điểm biên của ảnh Gray theo phép dò Canny",Ie[179,123])
if Ie[181][120]==255:
 	print("diem bien anh(181,120) la diem bien theo Canny")
else:
 	print("diem bien anh (181,120) khong la diem anh the canny")
#5cua so (3, 3) : Tính cửa sổ lân cận
so_dong=I.shape[0]
so_cot=I.shape[1]
y= 181
x = 120
for k in range(-1, 2): #lan can (3, 3)
 	for l in range(-1,2):
 		if ((y+k) >= 0) & ((y+k)<=so_dong-1) & ((x+l) >= 0) & ((x+l)<=so_cot-1):
 			print("muc xam",Ig[y+k,x+l])
#6 Otsu 
nguong_otsu, Ib = cv2.threshold(Ig,0,255, cv2.THRESH_OTSU)
print("nguong: ",nguong_otsu)
cv2.imshow("anh nhi phan bang Otsu", Ib)
#xac dinh, ve contous
_, contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("anh co ve chu tuyen", I)
###################
cv2.waitKey()
