# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================

import cv2
import numpy as np

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

# 克隆
m1 = img.copy()

# 赋值
m2 = img
img[100:200, 200:300, :] = 255
cv2.imshow("m2", m2)

m3 = np.zeros(img.shape, img.dtype)
cv2.imshow("m3", m3)

m4 = np.zeros([512, 512], np.uint8)
cv2.imshow("m4", m4)

m5 = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
m5[:, :, 0] = 255
cv2.imshow("m5", m5)

cv2.waitKey(0)
cv2.destroyAllWindows()
