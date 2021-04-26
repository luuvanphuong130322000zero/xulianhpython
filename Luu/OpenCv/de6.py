#DE 6
import cv2
import numpy as np

# def avg_filt(Igray,d):
#  h=Igray.shape[0]
#  w=Igray.shape[1]
#  Igray_new=np.zeros((h,w),dtype='uint8')
#  for i in range(h):
#  for j in range(w):
#  g_sum=0
#  for k in range(-d,d+1):
#  for l in range(-d,d+1):
#  if (i+k>=0) &(i+k<=h-1) & (j+l>=0) &(j+l<=w-1):
#  g_sum=g_sum+Igray[i+k][j+l]
#  Igray_new[i][j]=g_sum//((2*d+1)*(2*d+1))
#  return Igray_new

def gian_muc_xam(Igray):
	a=np.min(Igray)
	b=np.max(Igray)
	w=Igray.shape[1]
	h=Igray.shape[0]
	for i in range(h):
		for j in range(w):
			Igray[i][j]=(255*int(Igray[i][j]-a))//(b-a)
			return a,b,Igray

I=cv2.imread('anh5.jpg')
#hienthi
cv2.imshow('Anh I',I)

#2
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('Kenh H cua Ihsv',Ihsv[:,:,0])

print('Muc sang lon nhat cua kenh S: ',np.max(Ihsv[:,:,1]))

#3
# Ihsv_S=Ihsv[:,:,1]
# Is=np.zeros((Ihsv.shape[0],Ihsv.shape[1],3), dtype='uint8')
# Is=avg_filt(Ihsv_S,3)
# cv2.imshow('Anh loc TBC',Is)

Is=cv2.blur(Ihsv[:,:,1],(7,7))
cv2.imshow('anh smooth trung binh cong',Is)

#4
Is=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
nguong,Ib= cv2.threshold(Is,0,255,cv2.THRESH_OTSU)
cv2.imshow('anh nguong OTSU',Ib)

#5
contours,_ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #tìm Countours
cv2.drawContours (I, contours, -1, (0,0,255),2) #vẽ Contours
cv2.imshow('anh co ve chu tuyen',I)

max_area=0.0
cnt_max=[]
for cnt in contours:
	if max_area < cv2.contourArea(cnt):
		max_area=cv2.contourArea(cnt)
		cnt_max=cnt
print('Dien tich Max: ',max_area)
#vẽ contour có diện tích max
cv2.drawContours (I, [cnt_max], -1, (255,0,255),2)  
cv2.imshow('anh co ve chu tuyen max',I) 

#6

a,b,Ir=gian_muc_xam(Ihsv[:,:,2])
Ihsv[:,:,2]=Ir
cv2.imshow('Kenh V gian muc xam ', Ihsv[:,:,2])

I=cv2.cvtColor(Ihsv,cv2.COLOR_HSV2BGR)
cv2.imshow('Hien thi lai anh I',I)
cv2.waitKey()
