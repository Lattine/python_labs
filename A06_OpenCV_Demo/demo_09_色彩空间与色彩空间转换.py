# -*- coding: utf-8 -*-

# @Time    : 2019/8/15
# @Author  : Lattine

# ======================
import cv2

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("BRG", img)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

# BGR to YUV
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("yuv", yuv)

# BGR to YCrCb
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow("YCrCb", ycrcb)

img2 = cv2.imread("data/dog.png")
cv2.imshow("dog", img2)
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (35, 43, 46), (99, 255, 255))
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
