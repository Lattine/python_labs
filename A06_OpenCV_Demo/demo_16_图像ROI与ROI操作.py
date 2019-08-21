# -*- coding: utf-8 -*-

# @Time    : 2019/8/21
# @Author  : Lattine

# ======================
import cv2
import numpy as np

img = cv2.imread("data/house.png")
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

h, w = img.shape[:2]

# ROI
cy = h // 2
cx = w // 2
roi = img[cy - 100:cy + 100, cx - 100:cx + 100, :]
cv2.imshow("roi 1", roi)

img_c = np.copy(roi)  # copy ROI
roi[:, :, 0] = 0  # modify ROI
cv2.imshow("origin", img)

img_c[:, :, 2] = 0  # modify copy roi
cv2.imshow("origin", img)
cv2.imshow("copy roi", img_c)

# example with ROI - generate mask
img = cv2.imread("data/dog.png")
cv2.imshow("dog", img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (35, 43, 46), (99, 255, 255))

# extract person ROI
mask = cv2.bitwise_not(mask)
roi = cv2.bitwise_and(img, img, mask=mask)

# generate background
result = np.zeros(img.shape, img.dtype)
result[:, :, 0] = 255

# combine background + roi
mask = cv2.bitwise_not(mask)
dst = cv2.bitwise_or(roi, result, mask=mask)
dst = cv2.add(dst, roi)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
