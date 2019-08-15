# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/house.png", 0)  # 读入
img = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow("Origin", img)

# ----- 静态Canny ------
canny = cv2.Canny(img, 50, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)

# ----- 动态Canny -----
import numpy as np


def CannyThreshold(img, gray, low_threshold=10, ratio=3, kernel_size=3):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, low_threshold, low_threshold * ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask=detected_edges)
    cv2.imshow("Canny Demo", dst)
    cv2.waitKey(0)


img = cv2.imread("data/house.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.createTrackbar("min threshold", "Canny Demo", 10, 100, CannyThreshold)
CannyThreshold(img, gray)

