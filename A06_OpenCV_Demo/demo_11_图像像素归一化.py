# -*- coding: utf-8 -*-

# @Time    : 2019/8/20
# @Author  : Lattine

# ======================
import cv2
import numpy as np

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 转为浮点数类型
gray = np.float32(gray)
print(gray)

# scale and shift by NORM_MINMAX
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv2.NORM_MINMAX)
print(dst)
cv2.imshow("NORM_MINMAX", np.uint8(dst * 255))

# scale and shift by NORM_INF
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_INF)
print(dst)
cv2.imshow("NORM_INF", dst)

# scale and shift by NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L1)
print(dst)
cv2.imshow("NORM_L1", np.uint8(dst * 10000000))

# scale and shift by NORM_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L2)
print(dst)
cv2.imshow("NORM_L2", np.uint8(dst * 10000))

cv2.waitKey(0)
cv2.destroyAllWindows()
