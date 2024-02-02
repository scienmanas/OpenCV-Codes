import cv2

cb_img = cv2.imread("checkerboard_18x18.png",0)
print(cb_img.shape)
# plt.imshow(cb_img, cmap='gray')
cv2.imshow('Image', cb_img)
cv2.waitKey(8000)