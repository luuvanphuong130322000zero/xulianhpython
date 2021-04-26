'''
Bài tập 24.
Đọc vào ảnh hoa1.jpg được biến ma trận ảnh I.

24a. Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Ihsv.
24b. Cân bằng histogram của kênh V của Ihsv. Hiển thị kênh V được cân bằng.
24c. Thay đổi kênh V của Ihsv thành kênh V đã cân bằng. Chuyển Ihsv về biểu diễn RGB được ảnh I2. Hiển thị I2.
24d. Ghi ma trận ảnh I2 thành file ảnh hoa1.png
24e. Giảm size ảnh xuống 1/2. Hiển thị ảnh đã giảm size.
24g. Làm trơn ảnh kênh H của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 7x7 được ảnh Ih. Hiển thị ảnh Ih.
24h. Nhị phân hóa anh Ih theo ngưỡng Otsu được ảnh nhị phân Ib. Hiển thị ảnh Ib.
24i. Tìm các contour của ảnh Ib. Vẽ các đường contour trên ảnh gốc I. Hiển thị ảnh I.
24k.Vẽ đường contour có diện tích lớn nhất ở câu 24i trên ảnh gốc I. Hiển thị ảnh I.
24l. Tìm kiếm biên theo thuật toán Canny của kênh S của ảnh Ihsv được ảnh nhị phân Ie. Hiển thị ảnh Ie.
24l. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  kênh S của ảnh Ihsv theo phép dò biên Canny không?
24n. Hiển thi các giá trị mức xám của kênh S của ảnh Ihsv trong lân cận cửa sổ 5x5 của pixel có tọa độ dòng y=312, cột x=279.
24o. Chuyển ảnh I sang ảnh grayscale theo công thức biến đổi bộ mầu (r,g,b) về mức xám=0.39*r+0.50*g+0.11*b, được ảnh Ig. Hiển thị ảnh Ig.
24p. Tìm kiếm biên theo thuật toán Canny của Ig được ảnh nhị phân Ie2. Hiển thị ảnh Ie2.
24q. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Canny không?
24r. Hiển thi các giá trị mức xám của ảnh Ig trong lân cận cửa sổ 5x5 của pixel có tọa độ dòng y=312, cột x=279.
24s. Xác định ma trận gradient theo hướng x của ảnh Ig với phương pháp Sobel được ảnh IgradientX. Hiển thi IgradientX.
24t. Xác định ma trận gradient theo hướng y của ảnh Ig với phương pháp Sobel được ảnh IgradientY. Hiển thi IgradientY.
24u. Xác định ma trận gradient của ảnh Ig theo cả 2 hướng y và hướng x với phương pháp Sobel được ảnh Igradient=(IgradientX^2+IgradientY^2)^0.5. Hiển thi Igradient.
24v. Xác định ảnh biên của ảnh Ig sử dụng phương pháp dò biên Sobel và ma trận gradient Igradient với ngưỡng quyết định điểm biên nguong_bien=1000, được ảnh nhị phân Ie3. Hiển thị ảnh Ie3.
24x. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Sobel trên không?
24y. Giãn mức xám của kênh V của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Iv2. Hiển thị ảnh Iv2.
24z. Giãn mức xám của kênh S của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Is2. Hiển thị ảnh Is2.
'''
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

#24r. Hiển thi các giá trị mức xám của ảnh Ig trong lân cận cửa sổ 5x5 của pixel có tọa độ dòng y=312, cột x=279.
''' 
import cv2
import numpy as np
import random

I = cv2.imread('I04.jpg')

matran_trongso= np.zeros((7,7),dtype='float32')
s=0.0
for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=random.random()
        s=s+matran_trongso[i][j]
for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=matran_trongso[i][j]/s

print(matran_trongso)
I_2 = cv2.filter2D(I,-1,matran_trongso)
cv2.imshow('loc trung binh co trong so',I_2)
'''
h=Ig.shape[0]
w=Ig.shape[1]
I_g=np.zeros((h,w,1),dtype='uint8')
I_g[:,:,0]=cv2.blur(Ig,(5,5))
#cv2.imshow('Loc trung binh anh Gray', I_g)
print("Giá trị mức xám ảnh lọc trung bình 5x5 của ảnh gray là:", I_g[312,279])
#24p. Tìm kiếm biên theo thuật toán Canny của Ig được ảnh nhị phân Ie2. Hiển thị ảnh Ie2.
Ie2 = cv2.Canny(Ig,0, 255)
#cv2.imshow("Canny image", Ie2)
#24q. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Canny không?
print("Điểm biên của ảnh Gray theo phép dò Canny",Ie2[312,279])
#24s. Xác định ma trận gradient theo hướng x của ảnh Ig với phương pháp Sobel được ảnh IgradientX. Hiển thi IgradientX.
laplacian = cv2.Laplacian(Ig,cv2.CV_64F)
IgradientX = cv2.Sobel(Ig,cv2.CV_64F,1,0,ksize=5)
IgradientY = cv2.Sobel(Ig,cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(Ig,cmap = 'gray')
plt.title('Ảnh gốc'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(IgradientX,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(IgradientY,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#plt.show()
#25u. Xác định ma trận gradient của ảnh Ig theo cả 2 hướng y và hướng x với phương pháp Sobel được ảnh Igradient=(IgradientX+IgradientY)//2. Hiển thi Igradient.
Igradient=(IgradientX+IgradientY)//2
#cv2.imshow("Igradient image", Igradient)

#24v. Xác định ảnh biên của ảnh Ig sử dụng phương pháp dò biên Sobel và ma trận gradient Igradient với ngưỡng quyết định điểm biên nguong_bien=30, được ảnh nhị phân Ie3. Hiển thị ảnh Ie3.
#24x. Kiểm tra pixel có tọa độ dòng y=312, cột x=279 có là điểm biên của  ảnh Ig theo phép dò biên Sobel trên không?
print("Điểm biên của ảnh Gray theo phép dò Sobel x",IgradientX[312,279])
print("Điểm biên của ảnh Gray theo phép dò Sobel y",IgradientX[279,312])

#24y. Giãn mức xám của kênh V của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Iv2. Hiển thị ảnh Iv2.
#Giãn mức xám của kênh S của ảnh Ihsv lên khoảng tối đa [0,255]
width=I.shape[1]
height=I.shape[0] 
a=Is[0][0]
b=Is[0][0]

for i in range(height):
    for j in range(width):
        if a> Is[i][j]:
            a=Is[i][j]
        if b < Is[i][j]:
            b=Is[i][j]
print([a,b])
for i in range(height):
    for j in range(width):
        Is[i][j]=(255* int(Is[i][j]-a))//(b-a)
#cv2.imshow('Gian muc xam kenh V',Iv)
cv2.imshow('Gian muc xam kenh S',Is)
#24z. Giãn mức xám của kênh S của ảnh Ihsv lên khoảng tối đa [0,255] được ảnh Is2. Hiển thị ảnh Is2.

cv2.waitKey()