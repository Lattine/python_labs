# -*- coding: utf-8 -*-

# @Time    : 2019/8/22
# @Author  : Lattine

# ======================

import cv2

src = cv2.imread("data/house.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("threshold", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv2.drawContours(src, contours, -1, (0, 0, 255), 2)
cv2.imshow("src with contours", src)

# area = cv2.contourArea(cnt) # 轮廓面积
# perimeter = cv2.arcLength(cnt, True) # 轮廓周长
# x, y, w, h = cv2.boundingRect(cnt) # 外接矩阵，不考虑旋转并且能包含整个轮廓的矩形。

# rect = cv2.minAreaRect(cnt) # 最小外接矩阵，考虑旋转
# 矩形四个角点取整
# box = np.int0(cv2.boxPoints(rect))

cv2.waitKey(0)
cv2.destroyAllWindows()
