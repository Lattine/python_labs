# -*- coding: utf-8 -*-

# @Time    : 2019/8/20
# @Author  : Lattine

# ======================
import cv2
import numpy as np

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

# X Flip 倒影
dst1 = cv2.flip(img, 0)
cv2.imshow("x-flip", dst1)

# Y Flip 镜像
dst2 = cv2.flip(img, 1)
cv2.imshow("y-flip", dst2)

# XY Flip 对角
dst3 = cv2.flip(img, -1)
cv2.imshow("xy-flip", dst3)

# CUSTOM-FLIP
h, w, ch = img.shape
dst = np.zeros(img.shape, img.dtype)
for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        dst[row, w - col - 1] = [b, g, r]
cv2.imshow("custom-y-flip", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
