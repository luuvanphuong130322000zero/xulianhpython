'''
Đọc vào ảnh hat1.png được biến ma trận ảnh I.
https://drive.google.com/open?id=1ZPqjrE47vx0pgy8NOgi7ddc3vDXfQ9aA&authuser=0

26a. Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Ihsv.
26b. Cân bằng histogram của kênh V của Ihsv. Hiển thị kênh V được cân bằng.
26c. Thay đổi kênh V của Ihsv thành kênh V đã cân bằng. Chuyển Ihsv về biểu diễn RGB được ảnh I2. Hiển thị I2.
26d. Ghi ma trận ảnh I2 thành file ảnh hoa1.png
26e. Giảm size ảnh xuống 1/4. Hiển thị ảnh đã giảm size.
26g. Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 7x7 được ảnh Is. Hiển thị ảnh Is.
26h. Nhị phân hóa ảnh (255- Is) (ảnh nghịch đảo độ sáng của Is, trắng -> đen; đen->trắng) theo ngưỡng Otsu được ảnh nhị phân Ib. Hiển thị ảnh Ib.
26i(bỏ qua do chưa học). Tìm các contour của ảnh Ib. Vẽ các đường contour trên ảnh gốc I. Hiển thị ảnh I.
26k(bỏ qua do chưa học).Vẽ đường contour có diện tích lớn nhất ở câu 26i trên ảnh gốc I. Hiển thị ảnh I.
26l. Tìm kiếm biên theo thuật toán Canny của kênh S của ảnh Ihsv được ảnh nhị phân Ie. Hiển thị ảnh Ie.
26l. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  kênh S của ảnh Ihsv theo phép dò biên Canny không?
26n. Hiển thi các giá trị mức xám của kênh S của ảnh Ihsv trong lân cận cửa sổ 5x5 của pixel có tọa độ dòng y=312, cột x=279.
26o. Chuyển ảnh I sang ảnh grayscale theo công thức biến đổi bộ mầu (r,g,b) về mức xám=0.39*r+0.50*g+0.11*b, được ảnh Ig. Hiển thị ảnh Ig.
26p. Tìm kiếm biên theo thuật toán Canny của Ig được ảnh nhị phân Ie2. Hiển thị ảnh Ie2.
26q. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Canny không?
26r. Hiển thi các giá trị mức xám của ảnh Ig trong lân cận cửa sổ 5x5 của pixel có tọa độ dòng y=312, cột x=279.
26s. Xác định ma trận gradient theo hướng x của ảnh Ig với phương pháp Sobel được ảnh IgradientX. Hiển thi IgradientX.
26t. Xác định ma trận gradient theo hướng y của ảnh Ig với phương pháp Sobel được ảnh IgradientY. Hiển thi IgradientY.
26u. Xác định ma trận gradient của ảnh Ig theo cả 2 hướng y và hướng x với phương pháp Sobel được ảnh Igradient=(IgradientX+IgradientY)//2. Hiển thi Igradient.
26v. Xác định ảnh biên của ảnh Ig sử dụng phương pháp dò biên Sobel và ma trận gradient Igradient với ngưỡng quyết định điểm biên nguong_bien=50, được ảnh nhị phân Ie3. Hiển thị ảnh Ie3.
26x. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Sobel trên không?
26y. Giãn mức xám của kênh V của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Iv2. Hiển thị ảnh Iv2.
26z. Giãn mức xám của kênh S của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Is2. Hiển thị ảnh Is2.

'''
#Đọc ảnh mầu anh5.jpg vào biến ma trận I. 
import cv2
import numpy as np
import matplotlib.pyplot as plt 

I=cv2.imread('anh5.jpg')
cv2.imshow('Anh goc:',I)

#Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Ihsv.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('Anh HSV:',Ihsv[:,:,0])

#Cân bằng histogram của kênh V của Ihsv. Hiển thị kênh V được cân bằng.
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

#Thay đổi kênh V của Ihsv thành kênh V đã cân bằng. Chuyển Ihsv về biểu diễn RGB được ảnh I2. Hiển thị I2.
I2 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("RGB", I2)

#Ghi ma trận ảnh I2 thành file ảnh hoa1.png
cv2.imwrite('hoa1.png', I2)

#Giảm size ảnh xuống 1/4. Hiển thị ảnh đã giảm size.
w=I.shape[1] //4
h=I.shape[0] //4
I_resize=cv2.resize(I, (w, h))
cv2.imshow('anh resize', I_resize)

# Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 7x7 được ảnh Is. Hiển thị ảnh Is.
for i in range(-3,4):
	for j in range(-3, 4):
		if (i>=0) & (i<= h-1) &(j>=0) &(j<= h-1):
			print(I[i,j,:])

#Nhị phân hóa ảnh (255- Is) (ảnh nghịch đảo độ sáng của Is, trắng -> đen; đen->trắng) theo ngưỡng Otsu được ảnh nhị phân Ib. Hiển thị ảnh Ib.
nguong=90
Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
Ib=np.zeros((Ig.shape[0],I.shape[1]),dtype='uint8')
for i in range(Ig.shape[0]):
    for j in range(I.shape[1]):
        if Ig[i][j] < nguong:
            Ib[i][j]=0#đen tuyệt đối
        else:
            Ib[i][j]=255#trắng tuyệt đối

#Tìm các contour của ảnh Ib. Vẽ các đường contour trên ảnh gốc I. Hiển thị ảnh I.
#Xác định các contours của ảnh Ib và vẽ đường contours lên ảnh gốc I với mầu đỏ tuyệt đối.
contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("anh co ve chu tuyen", I)

#Vẽ đường contour có diện tích lớn nhất ở câu 26i trên ảnh gốc I. Hiển thị ảnh I. 
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
cv2.imshow('anh co ve chu tuyen',I)           

#Tìm kiếm biên theo thuật toán Canny của kênh S của ảnh Ihsv được ảnh nhị phân Ie. Hiển thị ảnh Ie.
Ie = cv2.Canny(Ihsv[:,:,1],0,255)
cv2.imshow('anh nhi phan kenh S', Ie)

#Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  kênh S của ảnh Ihsv theo phép dò biên Canny không?
if Ie[312][279]==255:
	print("diem bien anh(312, 279) la diem bien theo Canny")
else:
	print("diem anh (312, 279) khong la diem anh the canny")

#Hiển thi các giá trị mức xám của kênh S của ảnh Ihsv trong lân cận cửa sổ 5x5 của pixel có tọa độ dòng y=312, cột x=279.
h=I.shape[0]
w=I.shape[1]
y=312
x=279
Is=Ihsv[:,:,1]
for k in range(-2, 3): #lan can (5, )
	for l in range(-1,2):
		if ((y+k) >= 0) & ((y+k)<=h-1) & ((x+l) >= 0) & ((x+l)<=w-1):
			print(Is[y+k,x+l])

#Chuyển ảnh I sang ảnh grayscale theo công thức biến đổi bộ mầu (r,g,b) về mức xám=0.39*r+0.50*g+0.11*b, được ảnh Ig. Hiển thị ảnh Ig.
Igray = np.zeros((h, w), dtype='uint8')
for i in range(h):
	for j in range(w):
		#gray=r*0.39+g*0.5+b*0.11
		d=39*int(I[i][j][2]) + 50*int(I[i][j][1]) + 11*int(I[i][j][0])
		d=d//100
		Igray[i][j]=d
cv2.imshow("anh graay", Igray)

#Tìm kiếm biên theo thuật toán Canny của Ig được ảnh nhị phân Ie2. Hiển thị ảnh Ie2.
Ie2 = cv2.Canny(Ig,0,255)
cv2.imshow('canny image: ',Ie2)

#Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Canny không?
if Ie2[312][279]==255:
	print("diem bien anh(312, 279) la diem bien theo Canny")
else:
	print("diem anh (312, 279) khong la diem anh the canny")

#Hiển thi các giá trị mức xám của ảnh Ig trong lân cận cửa sổ 5x5 của pixel có tọa độ dòng y=312, cột x=279.
so_dong=I.shape[0]
so_cot=I.shape[1]
y=312
x=279
for k in range(-2, 3): #lan can (5, )
	for l in range(-1,2):
		if ((y+k) >= 0) & ((y+k)<=so_dong-1) & ((x+l) >= 0) & ((x+l)<=so_cot-1):
			print(Ig[y+k,x+l])

#Xác định ma trận gradient theo hướng x của ảnh Ig với phương pháp Sobel được ảnh IgradientX. Hiển thi IgradientX.
sobelx = cv2.Sobel(Ig,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(Ig,cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(Ig,cmap = 'gray')
plt.title('Ảnh gốc'), plt.xticks([]), plt.yticks([])

plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

w = Igray.shape[1]
h = Igray.shape[0]
G = np.zeros((h, w), dtype= 'float64')
for i in range (h):
	for j in range (w):
		t1 = sobelx[i][j]*sobelx[i][j]
		t2 = sobely[i][j]*sobely[i][j]
		G[i][j]= np.sqrt(t1+t2)

#Xác định ảnh biên của ảnh Ig sử dụng phương pháp dò biên Sobel 
#và ma trận gradient Igradient với ngưỡng quyết định điểm biên nguong_bien=50, 
#được ảnh nhị phân Ie3. Hiển thị ảnh Ie3.
nguong = 50
Ie3 = np.zeros((h, w), dtype='uint8')
for i in range (h):
	for j in range (w):
		if G[i][j]>=nguong:
			Ie3[i][j]=255
		else:
			I[i][j]=0
cv2.imshow("bien G", Ie3)

#Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Sobel trên không?
if Ie3[312][279]==255:
	print("diem bien anh(312, 279) la diem bien theo Canny")
else:
	print("diem anh (312, 279) khong la diem anh the canny")

#Giãn mức xám của kênh V của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Iv2. Hiển thị ảnh Iv2.
Ir=Ihsv[:,:,2]
a=Ir[0][0]
b=Ir[0][0]

#Giãn mức xám của kênh S của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Is2. Hiển thị ảnh Is2.

Is2=Ihsv[:,:,1]
a=Is2[0][0]
b=Is2[0][0]

for i in range(h):
    for j in range(w):
        if a> Is2[i][j]:
            a=Is2[i][j]
        if b < Is2[i][j]:
            b=Is2[i][j]
print([a,b])
for i in range(h):
    for j in range(w):
        Ir[i][j]=(255* int(Is2[i][j]-a))//(b-a)
cv2.imshow('kenh S bien doi',Is2)

cv2.waitKey()