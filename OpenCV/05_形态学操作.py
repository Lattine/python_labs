# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================
import cv2

gray = cv2.imread("data/house.png", cv2.IMREAD_GRAYSCALE)

# -------------------- 腐蚀 --------------------
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
erosion = cv2.erode(gray, kernel)
cv2.imshow("erosion", erosion)

# -------------------- 膨胀 --------------------
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilation = cv2.dilate(gray, kernel)
cv2.imshow("dilation", dilation)

# -------------------- 轮廓 --------------------
outer = dilation - erosion
cv2.imshow("outer", outer)

# -------------------- 开运算 --------------------
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)

# -------------------- 闭运算 --------------------
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)

# -------------------- 形态学梯度 ------------------
gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("gradient", gradient)

# -----------------
cv2.waitKey(0)
cv2.destroyAllWindows()
