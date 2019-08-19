# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================

import cv2

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

dst = cv2.applyColorMap(img, cv2.COLORMAP_COOL)
cv2.imshow("output", dst)

# 伪色彩
img = cv2.imread("data/dog.png")
color_img = cv2.applyColorMap(img, cv2.COLORMAP_JET)
cv2.imshow("origin", img)
cv2.imshow("color img", color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
