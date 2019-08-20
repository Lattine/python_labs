# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2
import numpy as np

# create image one
src1 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src1[100:200, 100:200, 0] = 255
src1[100:200, 100:200, 1] = 255
cv2.imshow("src1", src1)

# create image two
src2 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
src2[100:200, 100:200, 2] = 255
cv2.imshow("src2", src2)

# 按位的逻辑操作，与、或、异或
dst_and = cv2.bitwise_and(src1, src2)
dst_or = cv2.bitwise_or(src1, src2)
dst_xor = cv2.bitwise_xor(src1, src2)

cv2.imshow("dst and", dst_and)
cv2.imshow("dst or", dst_or)
cv2.imshow("dst xor", dst_xor)

img = cv2.imread("data/house.png")
cv2.imshow("img", img)
dst_not = cv2.bitwise_not(img)  # 按位的逻辑操作，非
cv2.imshow("dst not", dst_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
