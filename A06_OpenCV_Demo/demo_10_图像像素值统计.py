# -*- coding: utf-8 -*-

# @Time    : 2019/8/20
# @Author  : Lattine

# ======================
import cv2
import numpy as np

img = cv2.imread("data/house.png", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("house", cv2.WINDOW_AUTOSIZE)
cv2.imshow("house", img)

min, max, min_loc, max_loc = cv2.minMaxLoc(img)
print("min {:.2f}, max: {:.2f}".format(min, max))
print("min loc: {}".format(min_loc))
print("max loc: {}".format(max_loc))

means, stddev = cv2.meanStdDev(img)
print("mean: {}, stddev: {}".format(means, stddev))
img[np.where(img < means)] = 0
img[np.where(img > means)] = 255
cv2.imshow("binary", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
