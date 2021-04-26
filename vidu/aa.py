img_blur = cv2.blur(img, ksize = (5, 5))
gradian_blur = cv2.GaussianBlur(img, ksize = (5, 5), sigmaX = 4, sigmaY=4)
cv2.imshow("Lam mo", img_blur)
cv2.imshow("Gaussian blur", gradian_blur)