# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2
import numpy as np

img1 = cv2.imread("data/house.png")
img2 = cv2.imread("data/dog.png")
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
h, w, ch = img1.shape

add_result = np.zeros(img1.shape, img1.dtype)
cv2.add(img1, img2, add_result)
cv2.imshow("add result", add_result)

sub_result = np.zeros(img1.shape, img1.dtype)
cv2.subtract(img1, img2, sub_result)
cv2.imshow("sub result", sub_result)

mul_result = np.zeros(img1.shape, img1.dtype)
cv2.multiply(img1, img2, mul_result)
cv2.imshow("mul result", mul_result)

div_result = np.zeros(img1.shape, img1.dtype)
cv2.divide(img1, img2, div_result)
cv2.imshow("div result", div_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
