# -*- coding: utf-8 -*-

# @Time    : 2019/8/14
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
